import numpy as np
import torch
import random 
import torch.nn.functional as F
from action import device, knowledge_based_action_bob

from environment import Create_Game

from DQN import DQN 
from LSTM import LSTM 

from LSTM_BOB import LSTM_BOB

Index_to_Action_tensor  = torch.tensor([(-1, 0), (1, 0), (0, -1), (0, 1)], dtype=torch.long, device=device)

class Memory_Array:
    def __init__(self, batch_size):
        self.batch_size     = batch_size
        self.sequences  = []
    
    def add_sequence(self, sequence):
        self.sequences.append(sequence)

    def ready(self):
        return len(self.sequences) >= self.batch_size
    
    def get_batch(self):
        batch = self.sequences[:self.batch_size]
        self.sequences = self.sequences[self.batch_size:]
        return batch

class Batch_Memory:
    def __init__(self, t_max, possible_positions, observation_size, first_hidden_state_size):
        self.max_size                           = t_max 
        self.possible_positions                 = possible_positions
        self.observation_size                   = observation_size
        self.first_hidden_state_size            = first_hidden_state_size

        self.observed_teammate_actions          = torch.zeros((self.max_size, self.observation_size),       dtype=torch.float32, device=device) 
        self.evader_belief_logit_map            = torch.zeros((self.max_size, self.possible_positions),     dtype=torch.float32, device=device)
        self.teammate_belief_logit_map          = torch.zeros((self.max_size, self.possible_positions),     dtype=torch.float32, device=device)
        self.first_hidden_state                 = torch.zeros((self.max_size, self.first_hidden_state_size),dtype=torch.float32, device=device)
       
        self.teammate_evader_belief_logit_map   = torch.zeros((self.max_size, self.possible_positions),     dtype=torch.float32, device=device)
        self.teammate_teammate_belief_logit_map = torch.zeros((self.max_size, self.possible_positions),     dtype=torch.float32, device=device)

        self.mask                               = torch.zeros((self.max_size,),     dtype=bool, device=device)


        self.index                              = 0


    def add_state(self, observed_teammate_actions, evader_belief_logit_map, teammate_belief_logit_map, first_hidden_state, teammate_evader_belief_logit_map, teammate_teammate_belief_logit_map):
        self.observed_teammate_actions[self.index]          = observed_teammate_actions
        self.evader_belief_logit_map[self.index]            = evader_belief_logit_map.squeeze(0)
        self.teammate_belief_logit_map[self.index]          = teammate_belief_logit_map.squeeze(0)
        self.first_hidden_state[self.index]                 = first_hidden_state.squeeze(0)
        
        self.teammate_evader_belief_logit_map[self.index]   = teammate_evader_belief_logit_map.squeeze(0)
        self.teammate_teammate_belief_logit_map[self.index] = teammate_teammate_belief_logit_map.squeeze(0)

        self.mask[self.index] = True                               

        self.index +=1

    def get_sequence(self):
        return (
            self.observed_teammate_actions,
            self.evader_belief_logit_map,
            self.teammate_belief_logit_map,
            self.first_hidden_state,
            self.teammate_evader_belief_logit_map,
            self.teammate_teammate_belief_logit_map,
            self.mask)
        

def loss(new_knowledge_model, new_knowledge_model_opt, batch):
    batch_size = len(batch)
    t_max = 50

    (observed_teammate_actions_batch, 
     evader_belief_logit_map_batch, 
     teammate_belief_logit_map_batch,
     first_hidden_state_batch,
     teammate_evader_belief_logit_map_batch,
     teammate_teammate_belief_logit_map_batch,
     mask_batch) = [torch.stack(bat, dim=0) for bat in zip(*batch)]

    hidden_state, cell_state = new_knowledge_model.init_state(batch_size)
    total_loss = 0.0
    total_count = mask_batch.sum()
    for t in range(t_max):
        hidden_state, cell_state, teammate_evader_logit, teammate_teammate_logit = new_knowledge_model(
            observed_teammate_actions_batch[:,t],
            evader_belief_logit_map_batch[:,t],
            teammate_belief_logit_map_batch[:,t],
            first_hidden_state_batch[:,t],
            hidden_state,
            cell_state,
        )

        teammate_evader_belief_loss = F.kl_div(
            F.log_softmax(teammate_evader_logit, dim=-1),
            F.softmax(teammate_evader_belief_logit_map_batch[:,t], dim=-1),
            reduction = "none"
        ).sum(dim=-1)

        teammate_teammate_belief_loss = F.kl_div(
            F.log_softmax(teammate_teammate_logit, dim=-1),
            F.softmax(teammate_teammate_belief_logit_map_batch[:,t], dim=-1),
            reduction = "none"
        ).sum(dim=-1)

        total_loss += ((teammate_evader_belief_loss + teammate_teammate_belief_loss) * mask_batch[:,t]).sum()

    total_loss = total_loss / total_count 
    total_loss.backward()
    new_knowledge_model_opt.step()

    return total_loss
    


def train(Agent):
    size                    = 15
    t_max                   = 50
    seed                    = 1
    simulations             = 30_000
    
    dqn_hidden_size         = 96
    new_lstm_hidden_size    = 192

    learning_rate           = 1e-4



    batch_size              = 64
    number_of_games         = 125
    possible_positions      = size*size
    

    epsilon  = 0

    number_of_updates   = 0


    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)

    p1_dqn = DQN(dqn_hidden_size, possible_positions, device).to(device)
    p1_dqn.load_state_dict(torch.load(Agent + "_dqn_lstm.pt", map_location=device))
    p1_dqn.stop()

    p2_dqn = DQN(dqn_hidden_size, possible_positions, device).to(device)
    p2_dqn.load_state_dict(torch.load(Agent + "_dqn_lstm.pt", map_location=device))
    p2_dqn.stop()

    p1_knowledge_model = LSTM(hidden_state_size = 96, possible_positions = possible_positions, device=device).to(device)
    p1_knowledge_model.load_state_dict(torch.load(Agent + "_lstm96.pt", map_location = device))
    p2_knowledge_model = LSTM(hidden_state_size = 96, possible_positions = possible_positions, device=device).to(device)
    p2_knowledge_model.load_state_dict(torch.load(Agent + "_lstm96.pt", map_location = device))

    p1_knowledge_model.stop()
    p2_knowledge_model.stop()
    # def __init__(self, first_hidden_state_size, hidden_state_size, possible_positions, device):
    new_knowledge_model = LSTM_BOB(first_hidden_state_size=96, hidden_state_size=new_lstm_hidden_size, possible_positions=possible_positions, device=device).to(device)
    new_knowledge_model_opt = torch.optim.AdamW(new_knowledge_model.parameters(), lr=learning_rate)

    games                   = [None]  * number_of_games

    p1_states               = [None]  * number_of_games
    p1_believes             = [None]  * number_of_games

    p2_states               = [None]  * number_of_games
    p2_believes             = [None]  * number_of_games

    steps                   = [0]     * number_of_games
    captured                = [False] * number_of_games

    sequence                = [None]  * number_of_games


    simulation              = 0
    completed_simulations   = 0

    captured_counter    = 0

    sequences = Memory_Array(batch_size)
    losses = 0

    def new_game(index):
        nonlocal simulation
        games[index] = Create_Game(size, t_max, seed+simulation)

        uni = torch.zeros((possible_positions,), dtype=torch.float32, device=device)

        p1_states[index]    = p1_knowledge_model.init_state()
        p1_believes[index]  = (uni.clone(), uni.clone())
        p2_states[index]    = p2_knowledge_model.init_state()
        p2_believes[index]  = (uni.clone(), uni.clone())
        sequence[index]    = Batch_Memory(t_max, possible_positions, observation_size=3, first_hidden_state_size=96)

        steps[index]      = 0    
        captured[index]   = False
        simulation += 1

    def terminal_helper(index):
        nonlocal completed_simulations
        nonlocal captured_counter 
        nonlocal number_of_updates
        nonlocal losses
        if sequence[index].index > 0:
            sequences.add_sequence(sequence[index].get_sequence())
        while(sequences.ready()):
            batch = sequences.get_batch()

            losses += loss(new_knowledge_model, new_knowledge_model_opt, batch)
            number_of_updates += 1
        if captured[index]:
            captured_counter    += 1
        
        completed_simulations   += 1

        if completed_simulations % 250 == 0 and completed_simulations > 0:
            print(f"For first {completed_simulations}, LSTM-BOB losses was {losses / number_of_updates}")
            losses              = 0
            captured_counter    = 0
            number_of_updates   = 0

        if simulation < simulations:
            new_game(index)
        else:
            games[index] = None


    def get_action(agent_id, observed_action):

        teammate_id = "P1" if agent_id == "P2" else "P2"
        for (observed_id, old_position, new_position) in (observed_action):
            if observed_id == teammate_id:
                return torch.tensor([1.0, (new_position[0] - old_position[0]), (new_position[1] - old_position[1])], device = device, dtype=torch.float32)
        return torch.tensor([0.0, 0.0, 0.0], device=device, dtype=torch.float32)

    for i in range(number_of_games):
        new_game(i)

    while(completed_simulations < simulations):
        running_indexes = [i for i in range(number_of_games) if games[i] is not None]
        running_games   = [games[i] for i in running_indexes]

        p1_observed_actions = [game.observe("P1", False)[1] for game in running_games]
        running_p1_states   = [p1_states[i] for i in running_indexes]
        p1_results = knowledge_based_action_bob("P1", running_games, p1_dqn, epsilon, running_p1_states,  p1_knowledge_model)
        p2_running_indexes = []

        for index, running_index in enumerate(running_indexes):
            (action, 
             hidden_state, 
             cell_state,
             evader_logits, 
             teammate_logits)  = p1_results[index]
            
            p1_states[running_index]    = (hidden_state, cell_state)
            p1_believes[running_index]  = (evader_logits, teammate_logits)

            if Agent == "p1":
                sequence[running_index].add_state(
                    observed_teammate_actions           = get_action("P1", p1_observed_actions[index]), 
                    evader_belief_logit_map             = evader_logits, 
                    teammate_belief_logit_map           = teammate_logits, 
                    first_hidden_state                  = hidden_state, 
                    teammate_evader_belief_logit_map    = p2_believes[running_index][0], 
                    teammate_teammate_belief_logit_map  = p2_believes[running_index][1])           


            steps[running_index]                += 1
            games[running_index].agent_move("P1", action)

            captured[running_index] = games[running_index].is_evader_captured()


            if captured[running_index] or steps[running_index] >= 2 * t_max:
                terminal_helper(running_index)
            else:
                p2_running_indexes.append(running_index)
        

        if p2_running_indexes:
            p2_running_games    = [games[i] for i in p2_running_indexes]
            p2_observed_actions = [game.observe("P2", False)[1] for game in p2_running_games]
            running_p2_states   = [p2_states[i] for i in p2_running_indexes]
            p2_results = knowledge_based_action_bob("P2", p2_running_games, p2_dqn, epsilon, running_p2_states, p2_knowledge_model)
        else:
            p2_results = []
        
        evader_running_index = []

        for index, running_index in enumerate(p2_running_indexes):
            (action, 
             hidden_state, 
             cell_state,
             evader_logits, 
             teammate_logits)  = p2_results[index]
            
            p2_states[running_index]    = (hidden_state, cell_state)
            p2_believes[running_index]  = (evader_logits, teammate_logits)

            if Agent == "p2":
                sequence[running_index].add_state(
                    observed_teammate_actions           = get_action("P2", p2_observed_actions[index]), 
                    evader_belief_logit_map             = evader_logits, 
                    teammate_belief_logit_map           = teammate_logits, 
                    first_hidden_state                  = hidden_state, 
                    teammate_evader_belief_logit_map    = p1_believes[running_index][0], 
                    teammate_teammate_belief_logit_map  = p1_believes[running_index][1])  


            steps[running_index] += 1
            games[running_index].agent_move("P2", action)

            captured[running_index] = games[running_index].is_evader_captured() 


            if captured[running_index] or steps[running_index] >= 2 * t_max:
                terminal_helper(running_index)
            else:
                evader_running_index.append(running_index)
        for index in evader_running_index:
            game = games[index]
            game.agent_move("E1", random.choice(game.valid_moves(game.agents["E1"].position)))
            captured[index] = game.is_evader_captured()
            if captured[index] or steps[index] >= 2 * t_max:
                terminal_helper(index)
            
            
            


    torch.save(new_knowledge_model.state_dict(), Agent + "_lstm_2nd.pt")
    return 1


if __name__ == "__main__":
    train("p1")
    train("p2")