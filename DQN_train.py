import numpy as np
import torch
import random 
import torch.nn.functional as F
from action import device, knowledge_based_action
from dataclasses import dataclass

from environment import Create_Game, Action_to_Index

from DQN import DQN 
from LSTM import LSTM 
from KBU import KBU


Index_to_Action_tensor  = torch.tensor([(-1, 0), (1, 0), (0, -1), (0, 1)], dtype=torch.long, device=device)
Index_to_Index_tensor   = torch.tensor([0, 1, 2, 3], dtype=torch.long, device=device).unsqueeze(1)

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

        self.action_memory                      = np.zeros(self.max_size, dtype=np.long)    
        self.reward_memory                      = np.zeros(self.max_size, dtype=np.float32)   
        self.captured_memory                    = np.zeros(self.max_size, dtype=np.long)       

        self.index          = 0
        self.current_size   = 0

    def add_transition(self, evader_probabilities_t0, teammate_probabilities_t0, agent_position_t0, evader_probabilities_t1, teammate_probabilities_t1, action, reward, captured):
        self.evader_probabilities_memory_t0[self.index]     = evader_probabilities_t0
        self.teammate_probabilities_memory_t0[self.index]   = teammate_probabilities_t0
        self.agent_position_memory_t0[self.index]           = agent_position_t0
        self.evader_probabilities_memory_t1[self.index]     = evader_probabilities_t1
        self.teammate_probabilities_memory_t1[self.index]   = teammate_probabilities_t1
        self.action_memory[self.index]                      = action
        self.reward_memory[self.index]                      = reward
        self.captured_memory[self.index]                    = captured

        self.index = self.index % self.max_size
        self.max_size  = min(self.max_size, self.max_size)

    def start_sampleing(self):
        return self.max_size >= self.start

    def sample(self, number_of_transitions):
        random_transitions = np.random.randint(0, self.max_size, size=number_of_transitions)

        return (
            torch.tensor(self.evader_probabilities_memory_t0[random_transitions], dtype=torch.float32, device=device),
            torch.tensor(self.teammate_probabilities_memory_t0[random_transitions], dtype=torch.float32, device=device),
            torch.tensor(self.agent_position_memory_t0[random_transitions], dtype=torch.float32, device=device),
            torch.tensor(self.evader_probabilities_memory_t1[random_transitions], dtype=torch.float32, device=device),
            torch.tensor(self.teammate_probabilities_memory_t1[random_transitions], dtype=torch.float32, device=device),
            self.action_memory[random_transitions],
            torch.tensor(self.reward_memory[random_transitions], dtype=torch.float32, device=device),
            torch.tensor(self.captured_memory[random_transitions], dtype=torch.float32, device=device),
        )


@dataclass
class state:
    evader_probability  : np.ndarray
    teammate_probability: np.ndarray
    agent_position      : np.ndarray
    agent_action        : float  
    reward              : float 
    captured            : bool




def loss(dqn, target_dqn, transitions, gamma):
    (evader_probabilities_t0s,
     teammate_probabilities_t0s,
     agent_position_t0s,
     evader_probabilities_t1s,
     teammate_probabilities_t1s,
     actions,
     rewards,
     captureds) = transitions

    q_values_t0         = dqn(evader_probabilities_t0s, teammate_probabilities_t0s, agent_position_t0s)
    agent_position_t1s  = agent_position_t0s + Index_to_Action_tensor[actions]
    action_value        = q_values_t0.gather(1, Index_to_Index_tensor[actions]).squeeze(1)

    with torch.no_grad():
        q_values_t1 = dqn(evader_probabilities_t1s, teammate_probabilities_t1s, agent_position_t1s)

        q_values_target_t1 = target_dqn(evader_probabilities_t1s, teammate_probabilities_t1s, agent_position_t1s)
        action_value_target = q_values_target_t1.gather(1, q_values_t1.argmax(dim=1).unsqueeze(1)).squeeze(1)

        loss = rewards + gamma * (1.0 - captureds) * action_value_target

    return F.smooth_l1_loss(action_value, loss)






def train(strategy):
    size                    = 15
    t_max                   = 50
    seed                    = 1
    simulations             = 2
    dqn_hidden_size         = 96


    learning_rate           = 3e-4
    gamma                   = 0.97
    distance_weight         = 0.9
    capture_bonus           = 350.0
    update_every_t_steps    = 2

    batch_size              = 64

    mem_size                = 120_000
    mem_start               = 5_000
    possible_positions      = size*size
    

    epsilon  = 1
    epsilon_min     = 0.05
    epsilon_decay   = 0.9998

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
        p1_knowledge_model = LSTM(hidden_state_size = 96, possible_positions = possible_positions, device=device).to(device)
        p1_knowledge_model.load_state_dict(torch.load(f"p1_lstm96.pt", map_location = device))
        p2_knowledge_model = LSTM(hidden_state_size = 96, possible_positions = possible_positions, device=device).to(device)
        p2_knowledge_model.load_state_dict(torch.load(f"p2_lstm96.pt", map_location = device))
    else:
        lstm = False
        p1_knowledge_model = KBU(size)
        p2_knowledge_model = KBU(size) 

    number_of_updates   = 0
    copy_to_target      = 1_000
    for simulation in range(simulations):
        game = Create_Game(size, t_max, seed+simulation)

        p1_state = p1_knowledge_model.init_state()
        p2_state = p2_knowledge_model.init_state()
        def step_loss(t):
            return -(1 + 10*(t / (t_max)))

        def pursuer_min_distance_to_evader():
            p1_position = game.agents["P1"].position
            p2_position = game.agents["P2"].position
            e1_position = game.agents["E1"].position
            def manhattan(pursuer, evader):
                return abs(pursuer[0] - evader[0]) + abs(pursuer[1] - evader[1])
            return min(manhattan(p1_position, e1_position), manhattan(p2_position, e1_position))

        captured            = False 
        captured_counter    = 0
        average_t           = 0
        p1state0            = None
        p1state0            = None


        for t in range(t_max):
            if captured:
                average_t           += t
                captured_counter    += 1
                captured            = False
                break 
            distance_before_actions = pursuer_min_distance_to_evader()

            p1_agent_position, p1_action, p1_evader_probability, p1_teammate_probability, p1_state = knowledge_based_action("P1", game, p1_dqn, epsilon, p1_state,  p1_knowledge_model, lstm)
            game.agent_move("P1", p1_action)

            p2_agent_position, p2_action, p2_evader_probability, p2_teammate_probability, p2_state = knowledge_based_action("P2", game, p2_dqn, epsilon, p2_state, p2_knowledge_model, lstm)
            game.agent_move("P2", p2_action)

            captured = game.is_evader_captured()
            if not captured:
                game.agent_move("E1", random.choice(game.valid_moves(game.agents["E1"].position)))

            distance_after_actions = pursuer_min_distance_to_evader()

            reward = step_loss(t) + distance_weight* (distance_before_actions - distance_after_actions)
            captured = game.is_evader_captured()
            if captured:
                reward += capture_bonus

            p1state1 = state(evader_probability  = p1_evader_probability,
                             teammate_probability= p1_teammate_probability,
                             agent_position      = p1_agent_position,
                             agent_action        = Action_to_Index[p1_action],
                             reward              = reward,
                             captured            = captured)
            p2state1 = state(evader_probability  = p2_evader_probability,
                             teammate_probability= p2_teammate_probability,
                             agent_position      = p2_agent_position,
                             agent_action        = Action_to_Index[p2_action],
                             reward              = reward,
                             captured            = captured)
            if p1state0 is not None:
                p1_memory.add_transition(evader_probabilities_t0    = p1state0.evader_probability, 
                                         teammate_probabilities_t0  = p1state0.teammate_probability, 
                                         agent_position_t0          = p1state0.agent_position,     
                                         evader_probabilities_t1    = p1state1.evader_probability, 
                                         teammate_probabilities_t1  = p1state1.teammate_probability,
                                         action                     = p1state0.agent_action, 
                                         reward                     = p1state0.reward, 
                                         captured                   = p1state0.captured)
                p2_memory.add_transition(evader_probabilities_t0    = p2state0.evader_probability, 
                                         teammate_probabilities_t0  = p2state0.teammate_probability, 
                                         agent_position_t0          = p2state0.agent_position,     
                                         evader_probabilities_t1    = p2state1.evader_probability, 
                                         teammate_probabilities_t1  = p2state1.teammate_probability,
                                         action                     = p2state0.agent_action, 
                                         reward                     = p2state0.reward, 
                                         captured                   = p2state0.captured)
            p1state0 = p1state1 
            p2state0 = p2state1 

            if p1_memory.start_sampleing() and t % update_every_t_steps == 0:
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

            epsilon = max(epsilon_min, epsilon * epsilon_decay)
        if simulation % 250 == 0:
            average_t           = 0
            captured_counter    = 0
            print(f"For {simulation - 250} to {simulation} the average t was {average_t}, and captures was {captured_counter / (250)}")

    torch.save(p1_dqn.state_dict(), f"p1_dqn_{strategy}.pt")
    torch.save(p2_dqn.state_dict(), f"p2_dqn_{strategy}.pt")
    return 1


if __name__ == "__main__":
    train("lstm")
    train("kbu")