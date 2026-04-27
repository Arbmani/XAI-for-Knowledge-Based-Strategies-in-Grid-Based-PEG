import numpy as np
import torch
import random 
import torch.nn.functional as F
from action import device, knowledge_based_action
from dataclasses import dataclass

from environment import Create_Game, Action_to_Index
from copy import copy

from DQN import DQN 
from LSTM import LSTM 
from KBU import KBU


Index_to_Action_tensor  = torch.tensor([(-1, 0), (1, 0), (0, -1), (0, 1)], dtype=torch.long, device=device)

class Experiance_Replay:
    def __init__(self, max_size, start, possible_positions):
        self.max_size               = max_size 
        self.start                  = start 
        self.possible_positions     = possible_positions

        self.evader_probabilities_memory_t0     = np.zeros((self.max_size, self.possible_positions), dtype=np.float32) 
        self.teammate_probabilities_memory_t0   = np.zeros((self.max_size, self.possible_positions), dtype=np.float32)
        self.agent_position_memory_t0           = np.zeros((self.max_size, 2), dtype=np.float32) 
        self.evader_probabilities_memory_t1     = np.zeros((self.max_size, self.possible_positions), dtype=np.float32) 
        self.teammate_probabilities_memory_t1   = np.zeros((self.max_size, self.possible_positions), dtype=np.float32)

        self.action_memory                      = np.zeros(self.max_size, dtype=np.int64)    
        self.reward_memory                      = np.zeros(self.max_size, dtype=np.float32)    
        self.terminal                           = np.zeros(self.max_size, dtype=np.int64)    
        self.time_left1                          = np.zeros(self.max_size, dtype=np.float32)   
        self.time_left2                          = np.zeros(self.max_size, dtype=np.float32) 

        self.index          = 0
        self.current_size   = 0

    def add_transition(self, evader_probabilities_t0, teammate_probabilities_t0, agent_position_t0, evader_probabilities_t1, teammate_probabilities_t1, action, reward, terminal, time_left1, time_left2):
        self.evader_probabilities_memory_t0[self.index]     = evader_probabilities_t0
        self.teammate_probabilities_memory_t0[self.index]   = teammate_probabilities_t0
        self.agent_position_memory_t0[self.index]           = agent_position_t0
        self.evader_probabilities_memory_t1[self.index]     = evader_probabilities_t1
        self.teammate_probabilities_memory_t1[self.index]   = teammate_probabilities_t1
        self.action_memory[self.index]                      = action
        self.reward_memory[self.index]                      = reward
        self.terminal[self.index]                           = terminal
        self.time_left1[self.index]                          = time_left1
        self.time_left2[self.index]                          = time_left2

        self.index = (self.index + 1) % self.max_size
        self.current_size  = min(self.current_size + 1, self.max_size)

    def start_sampleing(self):
        return self.current_size >= self.start

    def sample(self, number_of_transitions):
        random_transitions = np.random.randint(0, self.current_size, size=number_of_transitions)

        return (
            torch.tensor(self.evader_probabilities_memory_t0[random_transitions], dtype=torch.float32, device=device),
            torch.tensor(self.teammate_probabilities_memory_t0[random_transitions], dtype=torch.float32, device=device),
            torch.tensor(self.agent_position_memory_t0[random_transitions], dtype=torch.float32, device=device),
            torch.tensor(self.evader_probabilities_memory_t1[random_transitions], dtype=torch.float32, device=device),
            torch.tensor(self.teammate_probabilities_memory_t1[random_transitions], dtype=torch.float32, device=device),
            torch.tensor(self.action_memory[random_transitions], dtype=torch.long, device=device),
            torch.tensor(self.reward_memory[random_transitions], dtype=torch.float32, device=device),
            torch.tensor(self.terminal[random_transitions], dtype=torch.float32, device=device),
            torch.tensor(self.time_left1[random_transitions], dtype=torch.float32, device=device),
            torch.tensor(self.time_left2[random_transitions], dtype=torch.float32, device=device),
        )


@dataclass
class state:
    evader_probability  : np.ndarray
    teammate_probability: np.ndarray
    agent_position      : np.ndarray
    agent_action        : float  
    reward              : float 
    terminal            : bool
    time_left           : float


# made for games of size 15
def mask_illegals(agent_position_t1s):
    rows    = agent_position_t1s[:, 0]
    columns = agent_position_t1s[:, 1]

    mask = torch.zeros((agent_position_t1s.size(0), 4), dtype=torch.bool, device=agent_position_t1s.device)
    mask[:, 0] = rows > 0
    mask[:, 1] = rows < 14
    mask[:, 2] = columns > 0
    mask[:, 3] = columns < 14
    return mask


def loss(dqn, target_dqn, transitions, gamma):
    (evader_probabilities_t0s,
     teammate_probabilities_t0s,
     agent_position_t0s,
     evader_probabilities_t1s,
     teammate_probabilities_t1s,
     actions,
     rewards,
     terminal,
     time_left1,
     time_left2) = transitions

    q_values_t0         = dqn(evader_probabilities_t0s, teammate_probabilities_t0s, agent_position_t0s, time_left1)
    action_value        = q_values_t0.gather(1, actions.unsqueeze(1)).squeeze(1)

    target = rewards.clone()
    nonterminal = terminal == 0

    with torch.no_grad():
        if nonterminal.any().item():
            agent_position_t1s  = agent_position_t0s[nonterminal] + Index_to_Action_tensor[actions[nonterminal]]
            q_values_t1 = dqn(evader_probabilities_t1s[nonterminal], teammate_probabilities_t1s[nonterminal], agent_position_t1s, time_left2[nonterminal])
            q_values_target_t1 = target_dqn(evader_probabilities_t1s[nonterminal], teammate_probabilities_t1s[nonterminal], agent_position_t1s, time_left2[nonterminal])

            legal_mask = mask_illegals(agent_position_t1s) 
            q_values_t1 = q_values_t1.masked_fill(~legal_mask, -1e12)
            q_values_target_t1 = q_values_target_t1.masked_fill(~legal_mask, -1e12)

            action_value_target = q_values_target_t1.gather(1, q_values_t1.argmax(dim=1).unsqueeze(1)).squeeze(1)

            target[nonterminal] += gamma *  action_value_target

    return F.smooth_l1_loss(action_value, target)




def train(strategy):
    size                    = 15
    t_max                   = 50
    seed                    = 188_888_888
    simulations             = 500_000
    dqn_hidden_size         = 64


    learning_rate           = 1e-4
    gamma                   = 0.99

    step_cost               = -0.15

    capture_bonus           =  5
    no_capture_loss         = -8

    update_every_t_steps    = 8


    batch_size              = 128
    number_of_games         = 32

    mem_size                = 250_000
    mem_start               = 30_000
    possible_positions      = size*size
    

    epsilon  = 1
    epsilon_min     = 0.05
    epsilon_decay   = 0.999993

    number_of_updates   = 0
    copy_to_target      = 2_000

    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)



    p1_dqn = DQN(dqn_hidden_size, possible_positions, device).to(device)
    p1_dqn_target = DQN(dqn_hidden_size, possible_positions, device).to(device)
    p1_dqn_target.load_state_dict(p1_dqn.state_dict())
    p1_dqn_target.eval()
    p1_dqn_opt = torch.optim.Adam(p1_dqn.parameters(), lr=learning_rate)

    p2_dqn = DQN(dqn_hidden_size, possible_positions, device).to(device)
    p2_dqn_target = DQN(dqn_hidden_size, possible_positions, device).to(device)
    p2_dqn_target.load_state_dict(p2_dqn.state_dict())
    p2_dqn_target.eval()
    p2_dqn_opt = torch.optim.Adam(p2_dqn.parameters(), lr=learning_rate)


    p1_memory = Experiance_Replay(mem_size, mem_start, possible_positions)
    p2_memory = Experiance_Replay(mem_size, mem_start, possible_positions)
    
    if strategy == "lstm":
        lstm = True
        p1_knowledge_model = LSTM(hidden_state_size = 256, possible_positions = possible_positions, device=device).to(device)
        p1_knowledge_model.load_state_dict(torch.load(f"p1_lstm256.pt", map_location = device))
        p2_knowledge_model = LSTM(hidden_state_size = 256, possible_positions = possible_positions, device=device).to(device)
        p2_knowledge_model.load_state_dict(torch.load(f"p2_lstm256.pt", map_location = device))

        p1_knowledge_model.stop()
        p2_knowledge_model.stop()
    else:
        number_of_games = 1
        lstm = False
        p1_knowledge_model = KBU(size)
        p2_knowledge_model = KBU(size) 

    





    games                   = [None]  * number_of_games
    p1_knowledge_states     = [None]  * number_of_games
    p2_knowledge_states     = [None]  * number_of_games
    p1_states0              = [None]  * number_of_games
    p2_states0              = [None]  * number_of_games

    p1_states1_t              = [None]  * number_of_games
    p2_states1_t              = [None]  * number_of_games

    steps                   = [0]     * number_of_games
    captured                = [False] * number_of_games

    p1_agent_position       = [None]  * number_of_games
    p1_action               = [None]  * number_of_games
    p1_evader_probability   = [None]  * number_of_games
    p1_teammate_probability = [None]  * number_of_games

    p2_agent_position       = [None]  * number_of_games
    p2_action               = [None]  * number_of_games
    p2_evader_probability   = [None]  * number_of_games
    p2_teammate_probability = [None]  * number_of_games
    simulation_id           = [None]  * number_of_games

    simulation              = 0
    completed_simulations   = 0

    captured_counter    = 0
    average_steps       = 0

    added_transitions = 0
    def reward_func(game, agent_id):
        if game.is_evader_captured():
            return 0.0
    
        e  = game.agents["E1"].position
        p1 = game.agents["P1"].position
        p2 = game.agents["P2"].position
    
        d1 = abs(p1[0] - e[0]) + abs(p1[1] - e[1])
        d2 = abs(p2[0] - e[0]) + abs(p2[1] - e[1])

        if agent_id is not None:
            if agent_id == "P1":
                d2 = d2 * 0.5
            elif agent_id == "P2":
                d1 = d1 * 0.5
            else: 
                print("Error")
        
        return 0
        return (
            -(d1 + d2)         
        )
    

    p1_old_dist                   = [None]  * number_of_games
    p2_old_dist                   = [None]  * number_of_games

    def new_game(index):
        nonlocal simulation
        games[index] = Create_Game(size, t_max, seed+simulation)
        p1_knowledge_states[index] = p1_knowledge_model.init_state()
        p2_knowledge_states[index] = p2_knowledge_model.init_state()
        p1_states0[index] = None
        p2_states0[index] = None

        p1_states1_t[index] = None
        p2_states1_t[index] = None

        steps[index]      = 0    
        captured[index]   = False
        simulation_id[index] = simulation
        simulation += 1

    def add_transition_helper(memory, state0, state1):
        nonlocal added_transitions
        nonlocal number_of_updates

        memory.add_transition(
                        evader_probabilities_t0    = state0.evader_probability, 
                        teammate_probabilities_t0  = state0.teammate_probability, 
                        agent_position_t0          = state0.agent_position,     
                        evader_probabilities_t1    = state1.evader_probability, 
                        teammate_probabilities_t1  = state1.teammate_probability,
                        action                     = state0.agent_action, 
                        reward                     = state0.reward, 
                        terminal                   = state0.terminal,
                        time_left1                  = state0.time_left,
                        time_left2                  = state1.time_left,)
        added_transitions += 1
        if p1_memory.start_sampleing() and p2_memory.start_sampleing() and added_transitions % update_every_t_steps == 0 and added_transitions > 0:
            p1_loss = loss(p1_dqn, p1_dqn_target, p1_memory.sample(batch_size), gamma)
            p1_dqn_opt.zero_grad()
            p1_loss.backward()
            torch.nn.utils.clip_grad_norm_(p1_dqn.parameters(), 5.0)
            p1_dqn_opt.step()

            p2_loss = loss(p2_dqn, p2_dqn_target, p2_memory.sample(batch_size), gamma)
            p2_dqn_opt.zero_grad()
            p2_loss.backward()
            torch.nn.utils.clip_grad_norm_(p2_dqn.parameters(), 5.0)
            p2_dqn_opt.step()
            number_of_updates += 1
            if number_of_updates % copy_to_target == 0:
                p1_dqn_target.load_state_dict(p1_dqn.state_dict())
                p2_dqn_target.load_state_dict(p2_dqn.state_dict())

    def terminal_helper(index, extra_reward =0.0):
        nonlocal completed_simulations
        nonlocal captured_counter 
        nonlocal average_steps
        nonlocal epsilon


        if p1_states0[index] is not None:
            if p1_states1_t[index] is not None and p1_states0[index].time_left != p1_states1_t[index].time_left:
                add_transition_helper(p1_memory, p1_states1_t[index], p1_states0[index])

            terminal_state          = copy(p1_states0[index])
            terminal_state.reward   = extra_reward
            terminal_state.terminal = True
            add_transition_helper(p1_memory, terminal_state, terminal_state)
        if p2_states0[index] is not None:
            if p2_states1_t[index] is not None and p2_states0[index].time_left != p2_states1_t[index].time_left:
                add_transition_helper(p2_memory, p2_states1_t[index], p2_states0[index])

            terminal_state          = copy(p2_states0[index])
            terminal_state.reward   = extra_reward
            terminal_state.terminal = True
            add_transition_helper(p2_memory, terminal_state, terminal_state)

        if captured[index]:
            captured_counter    += 1
        completed_simulations   += 1
        average_steps           += steps[index]
        epsilon                 =  max(epsilon_min, epsilon * epsilon_decay)
        if completed_simulations % 250 == 0 and completed_simulations > 0:
            print(f"For first {completed_simulations}, epsilon is {epsilon:.3f}, captures was {(captured_counter / (250)):.3f}, average steps is {(average_steps / 250):.3f}, number of updates: {number_of_updates}")
            captured_counter    = 0
            average_steps       = 0
        if simulation < simulations:
            new_game(index)
        else:
            games[index] = None


    for i in range(number_of_games):
        new_game(i)

    while(completed_simulations < simulations):
        running_indexes = [i for i in range(number_of_games) if games[i] is not None]
        running_games   = [games[i] for i in running_indexes]

        p1_results = knowledge_based_action("P1", running_games, p1_dqn, epsilon, [p1_knowledge_states[i] for i in running_indexes] if lstm else [None]*len(running_indexes),  p1_knowledge_model, lstm, [steps[i] / (2 * t_max) for i in running_indexes])
        p2_running_indexes = []

        for index, running_index in enumerate(running_indexes):
            (p1_agent_position[running_index], 
             p1_action[running_index], 
             p1_evader_probability[running_index], 
             p1_teammate_probability[running_index], 
             p1_knowledge_states[running_index]
             )  = p1_results[index]
            p1_old_dist[running_index] = reward_func(games[running_index], "P1")


            steps[running_index]                += 1
            games[running_index].agent_move("P1", p1_action[running_index])



            captured[running_index] = games[running_index].is_evader_captured()
            terminal = captured[running_index] or (steps[running_index] >= 2 * t_max)
            p1_states1 = state(
                                evader_probability  = p1_evader_probability[running_index],
                                teammate_probability= p1_teammate_probability[running_index],
                                agent_position      = p1_agent_position[running_index],
                                agent_action        = Action_to_Index[p1_action[running_index]],
                                reward              = step_cost,
                                terminal            = terminal,
                                time_left           = (steps[running_index] / (2 * t_max)))
            if p1_states0[running_index] is not None:
            #    add_transition_helper(p1_memory, p1_states0[running_index], p1_states1)
                p1_states1_t[running_index]  = copy(p1_states0[running_index])
            p1_states0[running_index]  = p1_states1

            if terminal:
                if captured[running_index]:
                    terminal_helper(running_index, capture_bonus )#+3*15 *(2*t_max - steps[running_index]))
                else:
                    terminal_helper(running_index, no_capture_loss)
            else:
                p2_running_indexes.append(running_index)
        

        if p2_running_indexes:
            p2_running_games   = [games[i] for i in p2_running_indexes]
            p2_results = knowledge_based_action("P2", p2_running_games, p2_dqn, epsilon, [p2_knowledge_states[i] for i in p2_running_indexes] if lstm else [None]*len(p2_running_indexes), p2_knowledge_model, lstm, [steps[i] / (2 * t_max) for i in p2_running_indexes])
        else:
            p2_results = []
        
        evader_running_index = []

        for index, running_index in enumerate(p2_running_indexes):
            p2_old_dist[running_index] = reward_func(games[running_index], "P2")
            (p2_agent_position[running_index], 
             p2_action[running_index], 
             p2_evader_probability[running_index], 
             p2_teammate_probability[running_index], 
             p2_knowledge_states[running_index]
             ) = p2_results[index]
            

            steps[running_index] += 1
            games[running_index].agent_move("P2", p2_action[running_index])


            captured[running_index] = games[running_index].is_evader_captured() 
            terminal = captured[running_index] or (steps[running_index] >= 2 * t_max)
            p2_states1 = state(
                    evader_probability  = p2_evader_probability[running_index],
                    teammate_probability= p2_teammate_probability[running_index],
                    agent_position      = p2_agent_position[running_index],
                    agent_action        = Action_to_Index[p2_action[running_index]],
                    reward              = step_cost,
                    terminal            = terminal,
                    time_left           = (steps[running_index] / (2 * t_max)))
            if p2_states0[running_index] is not None:
            #    add_transition_helper(p2_memory, p2_states0[running_index], p2_states1)
                p2_states1_t[running_index] = copy(p2_states0[running_index])
            p2_states0[running_index] = p2_states1


            if terminal:
                if captured[running_index]:
                    terminal_helper(running_index, capture_bonus )#+ 3*15 *(2*t_max - steps[running_index]))
                else:
                    terminal_helper(running_index, no_capture_loss)
            else:
                evader_running_index.append(running_index)
        for index in evader_running_index:
            game = games[index]
            game.agent_move("E1", random.choice(game.valid_moves(game.agents["E1"].position)))
            captured[index] = game.is_evader_captured()
            if captured[index]:
                terminal_helper(index, capture_bonus )#+ 3*15 *(2*t_max - steps[index]))
            elif steps[index] >= 2 * t_max:
                terminal_helper(index, no_capture_loss)
            else:
                #p1_states0[index].reward = -0.1
                #p2_states0[index].reward = -0.1
                if p1_states1_t[index] is not None:

                    add_transition_helper(p1_memory, p1_states1_t[index], p1_states0[index])
                    add_transition_helper(p2_memory, p2_states1_t[index], p2_states0[index])

            
            


    torch.save(p1_dqn.state_dict(), f"p1_dqn_{strategy}.pt")
    torch.save(p2_dqn.state_dict(), f"p2_dqn_{strategy}.pt")
    return 1


if __name__ == "__main__":
    #train("lstm")
    train("kbu")