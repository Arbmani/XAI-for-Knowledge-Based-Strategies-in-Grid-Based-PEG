import numpy as np
import torch
import random 
import torch.nn.functional as F
from action import device, knowledge_based_action_bob_dqn, knowledge_based_action, get_observation
from dataclasses import dataclass

from interpretable_strategy_P1_first_order import interpretable_action as ia1
from interpretable_strategy_P2_first_order import interpretable_action as ia2

from environment import Create_Game, Action_to_Index
from copy import copy

from DQN_BOB    import DQN_BOB 
from DQN        import DQN 
from LSTM       import LSTM 
from LSTM_BOB   import LSTM_BOB
from KBU import KBU

Index_to_Action_tensor  = torch.tensor([(-1, 0), (1, 0), (0, -1), (0, 1)], dtype=torch.long, device=device)

@dataclass
class state:
    evader_probability  : np.ndarray
    teammate_probability: np.ndarray
    teammate_evader_probability  : np.ndarray
    teammate_teammate_probability: np.ndarray
    agent_position      : np.ndarray
    agent_action        : float  
    reward              : float 
    terminal            : bool






def validate(strategy):
    size                    = 15
    t_max                   = 50
    seed                    = 99499112
    simulations             = 40_000
    dqn_hidden_size         = 128



    gamma                   = 0.97

    capture_bonus           = 1
    no_capture_loss         = -25
    update_every_t_steps    = 4


    batch_size              = 125
    number_of_games         = 125

    possible_positions      = size*size
    

    epsilon  = 0

    number_of_updates   = 0
    copy_to_target      = 1_000

    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)

    if strategy == "BOB":
        p1_dqn = DQN_BOB(dqn_hidden_size, possible_positions, device).to(device)
        p1_dqn.load_state_dict(torch.load(f"p1_dqn_boblstm.pt", map_location = device))
        p1_dqn.eval()

        p2_dqn = DQN_BOB(dqn_hidden_size, possible_positions, device).to(device)
        p2_dqn.load_state_dict(torch.load(f"p2_dqn_boblstm.pt", map_location = device))
        p2_dqn.eval()


        p1_first_knowledge_model = LSTM(hidden_state_size = 256, possible_positions = possible_positions, device=device).to(device)
        p1_first_knowledge_model.load_state_dict(torch.load(f"p1_lstm256.pt", map_location = device))

        p1_second_knowledge_model = LSTM_BOB(first_hidden_state_size = 256, hidden_state_size = 512, possible_positions = possible_positions, device=device).to(device)
        p1_second_knowledge_model.load_state_dict(torch.load(f"p1_lstm_2nd.pt", map_location = device))

        p1_first_knowledge_model.stop()
        p1_second_knowledge_model.stop()


        p2_first_knowledge_model = LSTM(hidden_state_size = 256, possible_positions = possible_positions, device=device).to(device)
        p2_first_knowledge_model.load_state_dict(torch.load(f"p2_lstm256.pt", map_location = device))

        p2_second_knowledge_model = LSTM_BOB(first_hidden_state_size = 256, hidden_state_size = 512, possible_positions = possible_positions, device=device).to(device)
        p2_second_knowledge_model.load_state_dict(torch.load(f"p2_lstm_2nd.pt", map_location = device))

        p2_first_knowledge_model.stop()
        p2_second_knowledge_model.stop()

    elif strategy == "FIRST":
        p1_first_knowledge_model = LSTM(hidden_state_size = 256, possible_positions = possible_positions, device=device).to(device)
        p1_first_knowledge_model.load_state_dict(torch.load(f"p1_lstm256.pt", map_location = device))
        p2_first_knowledge_model = LSTM(hidden_state_size = 256, possible_positions = possible_positions, device=device).to(device)
        p2_first_knowledge_model.load_state_dict(torch.load(f"p2_lstm256.pt", map_location = device))

        p1_first_knowledge_model.stop()
        p2_first_knowledge_model.stop()

        p1_dqn = DQN(dqn_hidden_size, possible_positions, device).to(device)
        p1_dqn.load_state_dict(torch.load(f"p1_dqn_lstm.pt", map_location = device))
        p2_dqn = DQN(dqn_hidden_size, possible_positions, device).to(device)
        p2_dqn.load_state_dict(torch.load(f"p2_dqn_lstm.pt", map_location = device))
        p1_dqn.eval()
        p2_dqn.eval()
    elif strategy == "inter":
        p1_first_knowledge_model = LSTM(hidden_state_size = 256, possible_positions = possible_positions, device=device).to(device)
        p1_first_knowledge_model.load_state_dict(torch.load(f"p1_lstm256.pt", map_location = device))
        p2_first_knowledge_model = LSTM(hidden_state_size = 256, possible_positions = possible_positions, device=device).to(device)
        p2_first_knowledge_model.load_state_dict(torch.load(f"p2_lstm256.pt", map_location = device))

        p1_first_knowledge_model.stop()
        p2_first_knowledge_model.stop()
    elif strategy == "KBU":
        p1_knowledge_model = KBU(size)
        p2_knowledge_model = KBU(size) 

        p1_dqn = DQN(dqn_hidden_size, possible_positions, device).to(device)
        p1_dqn.load_state_dict(torch.load(f"p1_dqn_kbu.pt", map_location = device))
        p2_dqn = DQN(dqn_hidden_size, possible_positions, device).to(device)
        p2_dqn.load_state_dict(torch.load(f"p2_dqn_kbu.pt", map_location = device))


    games                           = [None]  * number_of_games

    p1_first_knowledge_states       = [None]  * number_of_games
    p1_second_knowledge_states      = [None]  * number_of_games
    p2_first_knowledge_states       = [None]  * number_of_games
    p2_second_knowledge_states      = [None]  * number_of_games

    steps                           = [0]     * number_of_games
    captured                        = [False] * number_of_games


    simulation                      = 0
    completed_simulations           = 0

    captured_counter                = 0
    average_steps                   = 0

    def manhattan(agent_1, agent_2):
        return abs(agent_1[0] - agent_2[0]) + abs(agent_1[1] - agent_2[1])

    def new_game(index):
        nonlocal simulation
        nonlocal strategy
        games[index] = Create_Game(size, t_max, seed+simulation)
        if strategy == "BOB":
            p1_first_knowledge_states[index]    = p1_first_knowledge_model.init_state()
            p1_second_knowledge_states[index]   = p1_second_knowledge_model.init_state()
            p2_first_knowledge_states[index]    = p2_first_knowledge_model.init_state()
            p2_second_knowledge_states[index]   = p2_second_knowledge_model.init_state()
        elif strategy == "FIRST" or strategy == "inter":
            p1_first_knowledge_states[index]    = p1_first_knowledge_model.init_state()
            p2_first_knowledge_states[index]    = p2_first_knowledge_model.init_state()

        steps[index]      = 0    
        captured[index]   = False

        simulation += 1

    def terminal_helper(index):
        nonlocal completed_simulations
        nonlocal captured_counter 
        nonlocal average_steps



        if captured[index]:
            captured_counter    += 1
        completed_simulations   += 1
        average_steps           += steps[index]
        if (completed_simulations) % simulations == 0 and completed_simulations > 0:
            print(f"For {completed_simulations}, epsilon is {epsilon}, captures was {(captured_counter / (simulations))}, average steps is {(average_steps / simulations)}",
                  f"Failed to capture was {simulations - captured_counter}")
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
        if strategy == "BOB":
            p1_results = knowledge_based_action_bob_dqn(
                "P1", 
                running_games, 
                p1_dqn, 
                epsilon, 
                [p1_first_knowledge_states[i] for i in running_indexes],  
                [p1_second_knowledge_states[i] for i in running_indexes], 
                p1_first_knowledge_model,
                p1_second_knowledge_model,
                [steps[i] / (2 * t_max) for i in running_indexes])
        elif strategy == "FIRST":
            p1_results = knowledge_based_action("P1", running_games, p1_dqn, epsilon, [p1_first_knowledge_states[i] for i in running_indexes], p1_first_knowledge_model, True, [steps[i] / (2 * t_max) for i in running_indexes])
        elif strategy == "KBU": 
            p1_results = knowledge_based_action("P1", running_games, p1_dqn, epsilon, [None]*len(running_indexes),  p1_knowledge_model, False, [steps[i] / (2 * t_max) for i in running_indexes])
        else:
            p1_results = []
        
        p2_running_indexes = []

        for index, running_index in enumerate(running_indexes):
            #results.append((agent_positions[i], action, 
            #                first_states[i], evader_probabilities[i], teammate_probabilities[i],
            #                second_states[i], teammate_evader_probabilities[i], teammate_teammate_probabilities[i]))
            if strategy == "BOB":
                (_, 
                 action, 
                 p1_first_knowledge_states[running_index],
                 _, 
                 _, 
                 p1_second_knowledge_states[running_index],
                 _, 
                 _, 
                 )  = p1_results[index]
            elif strategy == "FIRST":
                (_, 
                action, 
                _, 
                _, 
                p1_first_knowledge_states[running_index]
                ) = p1_results[index]
            elif strategy == "KBU":
                (_, 
                action, 
                _, 
                _, 
                _
                ) = p1_results[index]
            else:
                # evader_probability, teammate_probability, agent_position, time_left, lamda, size, valid_actions
                if strategy == "inter":
                    agent_position                  = games[running_index].agents["P1"].position
                    valid_moves                     = games[running_index].valid_moves(agent_position)  
                    hidden_state_0 = p1_first_knowledge_states[running_index][0].squeeze(0)
                    cell_state_0   = p1_first_knowledge_states[running_index][1].squeeze(0)

                    observation = get_observation("P1", games[running_index], delete_observed_actions_since_last_turn_array=True)
                    hidden_state_1, cell_state_1, evader_logits, teammate_logits = p1_first_knowledge_model(observation, hidden_state_0, cell_state_0)
                    p1_first_knowledge_states[running_index] = (hidden_state_1, cell_state_1)

                    evader_probabilities    = torch.softmax(evader_logits, dim=0)
                    teammate_probabilities  = torch.softmax(teammate_logits, dim=0)


                    action = ia1(evader_probabilities.cpu().numpy(), teammate_probabilities.cpu().numpy(), agent_position, (steps[i] / (2 * t_max)), 0.5, 15, valid_moves)
                else:
                    agent_position      = games[running_index].agents["P1"].position
                    valid_moves = games[running_index].valid_moves(agent_position)
                    best_action = valid_moves[0]
                    best_dist   = 15
                    for act in valid_moves:
                        new_position = games[running_index].new_position(agent_position, act)
                        new_dist     = manhattan(new_position, games[running_index].agents["E1"].position)
                        if new_dist < best_dist:
                            best_dist = new_dist
                            best_action = act
                    action = best_action
                    


            steps[running_index]                += 1
            games[running_index].agent_move("P1", action)
            captured[running_index] = games[running_index].is_evader_captured()
            if captured[running_index] or steps[running_index] >= 2 * t_max :
                terminal_helper(running_index)
            else:
                p2_running_indexes.append(running_index)
        

        if p2_running_indexes:
            p2_running_games   = [games[i] for i in p2_running_indexes]
            if strategy == "BOB":
                p2_results = knowledge_based_action_bob_dqn(
                    "P2", 
                    p2_running_games, 
                    p2_dqn, 
                    epsilon, 
                    [p2_first_knowledge_states[i] for i in p2_running_indexes],  
                    [p2_second_knowledge_states[i] for i in p2_running_indexes], 
                    p2_first_knowledge_model,
                    p2_second_knowledge_model,
                    [steps[i] / (2 * t_max) for i in p2_running_indexes])
                #p2_results = knowledge_based_action("P2", p2_running_games, p2_dqn, epsilon, [p2_knowledge_states[i] for i in p2_running_indexes] if lstm else [None]*len(p2_running_indexes), p2_knowledge_model, lstm)
            elif strategy == "FIRST":
                p2_results = knowledge_based_action("P2", p2_running_games, p2_dqn, epsilon, [p2_first_knowledge_states[i] for i in p2_running_indexes], p2_first_knowledge_model, True, [steps[i] / (2 * t_max) for i in p2_running_indexes])
            elif strategy == "KBU":
                p2_results = knowledge_based_action("P2", p2_running_games, p2_dqn, epsilon, [None]*len(p2_running_indexes), p2_knowledge_model, False, [steps[i] / (2 * t_max) for i in p2_running_indexes])
            else:
                p2_results = []
        else:
            p2_results = []
        
        evader_running_index = []

        for index, running_index in enumerate(p2_running_indexes):
            if strategy == "BOB":
                (_, 
                 action, 
                 p2_first_knowledge_states[running_index],
                 _, 
                 _, 
                 p2_second_knowledge_states[running_index],
                 _, 
                 _, 
                 )  = p2_results[index]
            elif strategy == "FIRST":
                (_, 
                action, 
                _, 
                _, 
                p2_first_knowledge_states[running_index]
                ) = p2_results[index]
            elif strategy == "KBU":
                (_, 
                action, 
                _, 
                _, 
                p2_first_knowledge_states[running_index]
                ) = p2_results[index]
            else:
                if strategy == "inter":
                    agent_position                  = games[running_index].agents["P2"].position
                    valid_moves                     = games[running_index].valid_moves(agent_position)  
                    hidden_state_0 = p2_first_knowledge_states[running_index][0].squeeze(0)
                    cell_state_0   = p2_first_knowledge_states[running_index][1].squeeze(0)

                    observation = get_observation("P2", games[running_index], delete_observed_actions_since_last_turn_array=True)
                    hidden_state_1, cell_state_1, evader_logits, teammate_logits = p2_first_knowledge_model(observation, hidden_state_0, cell_state_0)
                    p2_first_knowledge_states[running_index] = (hidden_state_1, cell_state_1)

                    evader_probabilities    = torch.softmax(evader_logits, dim=0)
                    teammate_probabilities  = torch.softmax(teammate_logits, dim=0)


                    action = ia2(evader_probabilities.cpu().numpy(), teammate_probabilities.cpu().numpy(), agent_position, (steps[i] / (2 * t_max)), 0.5, 15, valid_moves)
                else:
                    agent_position      = games[running_index].agents["P2"].position
                    valid_moves = games[running_index].valid_moves(agent_position)
                    best_action = valid_moves[0]
                    best_dist   = 15
                    for act in valid_moves:
                        new_position = games[running_index].new_position(agent_position, act)
                        new_dist     = manhattan(new_position, games[running_index].agents["E1"].position)
                        if new_dist < best_dist:
                            best_dist = new_dist
                            best_action = act
                    action = best_action


            steps[running_index] += 1
            games[running_index].agent_move("P2", action)
            captured[running_index] = games[running_index].is_evader_captured()

            if captured[running_index] or steps[running_index] >= 2 * t_max :
                terminal_helper(running_index)
            else:
                evader_running_index.append(running_index)
        for index in evader_running_index:
            game = games[index]

            game.agent_move("E1", random.choice(game.valid_moves(game.agents["E1"].position)))
            captured[index] = games[index].is_evader_captured()
            if captured[index] or steps[index] >= 2 * t_max :
                terminal_helper(index)
            

    return 1


if __name__ == "__main__":
    #validate("BOB")
    #validate("FIRST")
    #validate("naive")
    #validate("inter")
    validate("KBU")