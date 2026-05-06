import numpy as np
import torch
import random 
import torch.nn.functional as F
from action import device, knowledge_based_action_bob_dqn, knowledge_based_action, get_observation
from dataclasses import dataclass

import json

from interpretable_strategy_P1_first_order_512 import interpretable_action as ia1
from interpretable_strategy_P2_first_order_512 import interpretable_action as ia2

from interpretable_strategy_P1_first_order_KBU_512 import interpretable_action as ia1_KBU
from interpretable_strategy_P2_first_order_KBU_512 import interpretable_action as ia2_KBU

from interpretable_strategy_P1_second_order_512 import interpretable_action as ia1_2nd
from interpretable_strategy_P2_second_order_512 import interpretable_action as ia2_2nd

from environment import Create_Game, Action_to_Index
from copy import copy

from DQN_BOB    import DQN_BOB 
from DQN        import DQN 
from LSTM       import LSTM 
from LSTM_BOB   import LSTM_BOB
from KBU import KBU

Index_to_Action_tensor  = torch.tensor([(-1, 0), (1, 0), (0, -1), (0, 1)], dtype=torch.long, device=device)
from typing import Optional
@dataclass
class state:
    evader_probability                  : Optional[np.ndarray] = None  
    teammate_probability                : Optional[np.ndarray] = None
    teammate_evader_probability         : Optional[np.ndarray] = None
    teammate_teammate_probability       : Optional[np.ndarray] = None
    agent_position                      : Optional[np.ndarray] = None
    agent_action                        : Optional[float] = None
    reward                              : Optional[float] = None
    terminal                            : Optional[bool] = None

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def create_plot(p1_state_vector, p2_state_vector, e1_state_vector, strategy):

    if strategy == "BOB" or strategy == "inter2":
        maps = 4
        names = [
            "evader_probability",
            "teammate_probability",
            "teammate_evader_probability",
            "teammate_teammate_probability"]
    else:
        maps = 2

        names = [
            "evader_probability",
            "teammate_probability",]

    fig, map_array = plt.subplots(1, maps*2 + 1, figsize=(30, 6), constrained_layout=True)

    name_to_plot_names = {
        "evader_probability"            : "Evader",
        "teammate_probability"          : "Teammate",
        "teammate_evader_probability"   : "Teammate(Evader)",
        "teammate_teammate_probability" : "Teammate(Teammate)",

    }

    def frame(t):
        p1, p2, e1, = p1_state_vector[t], p2_state_vector[t], e1_state_vector[t]

        for belief_map in map_array:
            belief_map.clear()

        for i, (belief_map, belief_map_probs, name) in enumerate(zip(map_array[:2*maps], [p1]*maps + [p2]*maps, names*2)):
            belief = getattr(belief_map_probs, name)
            if torch.is_tensor(belief):
                belief = belief.cpu()

            belief_map.imshow(belief.reshape(15,15), cmap="viridis")
                
            belief_map.set_title(("P1(" if i < maps else "P2(") + name_to_plot_names[name] + ")", fontsize=14)
            belief_map.set_xlim(-0.5, 15 -0.5)
            belief_map.set_ylim(-0.5, 15 -0.5)
            belief_map.set_xticks(np.arange(-0.5, 15, 1))
            belief_map.set_yticks(np.arange(-0.5, 15, 1))
            belief_map.grid(True, linewidth=2)

        map_array[2*maps].set_title("GAME", fontsize=20)
        map_array[2*maps].set_xlim(-0.5, 15 -0.5)
        map_array[2*maps].set_ylim(-0.5, 15 -0.5)
        map_array[2*maps].set_xticks(np.arange(-0.5, 15, 1))
        map_array[2*maps].set_yticks(np.arange(-0.5, 15, 1))

        map_array[2*maps].grid(True, linewidth=2)

        r1, c1 = p1.agent_position
        r2, c2 = p2.agent_position
        er1, ec1 = e1.agent_position

        map_array[2*maps].scatter(c1, r1, edgecolors="black", s=300, marker="s")
        map_array[2*maps].scatter(c2, r2, edgecolors="black",s=300, marker="s")
        map_array[2*maps].scatter(ec1, er1, edgecolors="black", s=300, marker="o")

        map_array[2*maps].text(c1, r1, "P1", fontsize=12, ha="center", va="center")
        map_array[2*maps].text(c2, r2, "P2", fontsize=12, ha="center", va="center")
        map_array[2*maps].text(ec1, er1, "E1",fontsize=12,  ha="center", va="center")

        map_array[2*maps].set_box_aspect(1)


        return map_array 
    animation = FuncAnimation(fig, 
                              frame, 
                              frames=min(len(p1_state_vector), len(e1_state_vector),len(p2_state_vector)),
                            interval = 1000/3, blit=False)
    animation.save(strategy+".gif", writer="pillow", fps= 6)
    plt.close(fig)


    return # TODO



def validate(strategy, make_gif = False):
    size                    = 15
    t_max                   = 50
    seed                    = 99499112
    simulations             = 1_000_000
    dqn_hidden_size         = 128



    number_of_games         = 125

    possible_positions      = size*size
    

    epsilon  = 0


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
    elif strategy == "inter2":
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

    elif strategy == "KBU":
        number_of_games         = 1
        p1_first_knowledge_model = KBU(size)
        p2_first_knowledge_model = KBU(size) 

        p1_dqn = DQN(dqn_hidden_size, possible_positions, device).to(device)
        p1_dqn.load_state_dict(torch.load(f"p1_dqn_kbu.pt", map_location = device))
        p2_dqn = DQN(dqn_hidden_size, possible_positions, device).to(device)
        p2_dqn.load_state_dict(torch.load(f"p2_dqn_kbu.pt", map_location = device))

    elif strategy == "interKBU":
        number_of_games         = 1
        p1_first_knowledge_model = KBU(size)
        p2_first_knowledge_model = KBU(size) 


    games                           = [None]  * number_of_games

    p1_first_knowledge_states       = [None]  * number_of_games
    p1_second_knowledge_states      = [None]  * number_of_games
    p2_first_knowledge_states       = [None]  * number_of_games
    p2_second_knowledge_states      = [None]  * number_of_games

    game_seed                       = [None]   * number_of_games

    steps                           = [0]     * number_of_games
    captured                        = [False] * number_of_games


    simulation                      = 0
    completed_simulations           = 0

    captured_counter                = 0
    average_steps                   = 0

    if make_gif:
        number_of_games = 1
        simulations = 1
        p1_state_vector = []
        p2_state_vector = []
        e1_state_vector = []


    def manhattan(agent_1, agent_2, return_XnY = False):
        if return_XnY:
            return abs(agent_1[0] - agent_2[0]) + abs(agent_1[1] - agent_2[1]), abs(agent_1[0] - agent_2[0]), abs(agent_1[1] - agent_2[1])
        return abs(agent_1[0] - agent_2[0]) + abs(agent_1[1] - agent_2[1])

    def new_game(index):
        nonlocal simulation
        nonlocal strategy
        game_seed[index] = seed+simulation
        games[index] = Create_Game(size, t_max, game_seed[index])
        if strategy == "BOB" or strategy == "inter2":
            p1_first_knowledge_states[index]    = p1_first_knowledge_model.init_state()
            p1_second_knowledge_states[index]   = p1_second_knowledge_model.init_state()
            p2_first_knowledge_states[index]    = p2_first_knowledge_model.init_state()
            p2_second_knowledge_states[index]   = p2_second_knowledge_model.init_state()
        elif strategy == "FIRST" or strategy == "inter" or strategy == "KBU" or strategy == "interKBU":
            p1_first_knowledge_states[index]    = p1_first_knowledge_model.init_state()
            p2_first_knowledge_states[index]    = p2_first_knowledge_model.init_state()

        steps[index]      = 0    
        captured[index]   = False

        simulation += 1

    def terminal_helper(index):
        nonlocal completed_simulations
        nonlocal captured_counter 
        nonlocal average_steps
        nonlocal simulation

        if make_gif:
            create_plot(p1_state_vector, p2_state_vector, e1_state_vector,strategy)
        else:
            row_results = {
            "Model"     : strategy,
            "Seed"      : game_seed[index],
            "Captured"  : captured[index],
            "Steps"     : steps[index]
            }
            with open(f"Results_{strategy}.jsonl", "a") as file:
                file.write(json.dumps(row_results) + "\n")

        if captured[index]:
            captured_counter    += 1
        completed_simulations   += 1
        average_steps           += steps[index]


        if (completed_simulations) % simulations == 0 and completed_simulations > 0:
            print(f"{strategy}: after {completed_simulations}, epsilon is {epsilon}, captures was {(captured_counter / (simulations))}, average steps is {(average_steps / simulations)}",
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

        if strategy == "naive" and make_gif:
            evader_probabilities                    = torch.zeros(1, 225, device =device)  
            teammate_probabilities                  = torch.zeros(1, 225, device =device)  
            teammate_evader_probabilities           = torch.zeros(1, 225, device =device)  
            teammate_teammate_probabilities         = torch.zeros(1, 225, device =device)  

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
            p1_results = knowledge_based_action("P1", running_games, p1_dqn, epsilon, [None]*len(running_indexes),  p1_first_knowledge_model, False, [steps[i] / (2 * t_max) for i in running_indexes])
        else:
            p1_results = []
        
        p2_running_indexes = []

        for index, running_index in enumerate(running_indexes):
            #results.append((agent_positions[i], action, 
            #                first_states[i], evader_probabilities[i], teammate_probabilities[i],
            #                second_states[i], teammate_evader_probabilities[i], teammate_teammate_probabilities[i]))
            if strategy == "BOB":
                (agent_position, 
                 action, 
                 p1_first_knowledge_states[running_index],
                 evader_probabilities, 
                 teammate_probabilities, 
                 p1_second_knowledge_states[running_index],
                 teammate_evader_probabilities, 
                 teammate_teammate_probabilities, 
                 )  = p1_results[index]
            elif strategy == "FIRST":
                (agent_position, 
                action, 
                evader_probabilities, 
                teammate_probabilities, 
                p1_first_knowledge_states[running_index]
                ) = p1_results[index]
            elif strategy == "KBU":
                (agent_position, 
                action, 
                evader_probabilities, 
                teammate_probabilities, 
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


                    action = ia1(evader_probabilities.cpu().numpy(), teammate_probabilities.cpu().numpy(), agent_position, (steps[running_index]  / (2 * t_max)), 0.1, 15, valid_moves)
                elif strategy == "interKBU":
                    agent_position                  = games[running_index].agents["P1"].position
                    valid_moves                     = games[running_index].valid_moves(agent_position)  
                    evader_probabilities, teammate_probabilities = p1_first_knowledge_model.forward("P1", games[running_index]) 

                    action = ia1_KBU(evader_probabilities, teammate_probabilities, agent_position, (steps[running_index]  / (2 * t_max)), 0.1, 15, valid_moves)
                elif strategy == "inter2":
                    time_left = (steps[running_index] / (2 * t_max))
                    agent_position                  = games[running_index].agents["P1"].position
                    valid_moves                     = games[running_index].valid_moves(agent_position)  
                    hidden_state_0 = p1_first_knowledge_states[running_index][0].squeeze(0)
                    cell_state_0   = p1_first_knowledge_states[running_index][1].squeeze(0)

                    second_hidden_state_0 = p1_second_knowledge_states[running_index][0].squeeze(0)
                    second_cell_state_0   = p1_second_knowledge_states[running_index][1].squeeze(0)

                    observation, observed_action = get_observation("P1", games[running_index], delete_observed_actions_since_last_turn_array=True, get_action=True)
                    hidden_state_1, cell_state_1, evader_logits, teammate_logits = p1_first_knowledge_model(observation, hidden_state_0, cell_state_0)
                    second_hidden_state_1, second_cell_state_1, second_evader_logit, second_teammate_logit = p1_second_knowledge_model(observation.unsqueeze(0), observed_action.unsqueeze(0), evader_logits.unsqueeze(0), teammate_logits.unsqueeze(0), hidden_state_1.unsqueeze(0), cell_state_1.unsqueeze(0), second_hidden_state_0.unsqueeze(0), second_cell_state_0.unsqueeze(0), [time_left])


                    p1_first_knowledge_states[running_index] = (hidden_state_1, cell_state_1)
                    p1_second_knowledge_states[running_index] = (second_hidden_state_1, second_cell_state_1)
                    evader_probabilities    = torch.softmax(evader_logits, dim=0)
                    teammate_probabilities  = torch.softmax(teammate_logits, dim=0)

                    teammate_evader_probabilities    = torch.softmax(second_evader_logit.squeeze(0), dim=0)
                    teammate_teammate_probabilities  = torch.softmax(second_teammate_logit.squeeze(0), dim=0)

                    action = ia1_2nd(evader_probabilities.cpu().numpy(), teammate_probabilities.cpu().numpy(), teammate_evader_probabilities.cpu().numpy(), teammate_teammate_probabilities.cpu().numpy(), agent_position, time_left, 0.1, 15, valid_moves)

                else:

                    agent_position      = games[running_index].agents["P1"].position
                    valid_moves = games[running_index].valid_moves(agent_position)
                    best_action = valid_moves[0]
                    best_dist   = float("inf")
                    best_longest = float("inf")
                    for act in valid_moves:
                        new_position = games[running_index].new_position(agent_position, act)
                        new_dist, x_dist, y_dist     = manhattan(new_position, games[running_index].agents["E1"].position, True)
                        longest = max(x_dist, y_dist)
                        if new_dist <= best_dist and best_longest > longest:
                            best_dist = new_dist
                            best_action = act
                            best_longest = longest
                    action = best_action
                    

            if make_gif:
                if len(p1_state_vector) < 1:
                    if strategy == "BOB" or strategy == "inter2":
                        p2_stategif = state(
                            evader_probability  = evader_probabilities,
                            teammate_probability= teammate_probabilities,
                            teammate_evader_probability = teammate_evader_probabilities,
                            teammate_teammate_probability= teammate_teammate_probabilities, 
                            agent_position      =  games[0].agents["P2"].position)
                    else:
                        p2_stategif = state(
                            evader_probability  = evader_probabilities,
                            teammate_probability= teammate_probabilities,
                            agent_position      =  games[0].agents["P2"].position)
                        
                    e1_stategif = state(
                                agent_position      = games[0].agents["E1"].position)
                    p2_state_vector.append(p2_stategif)
                    e1_state_vector.append(e1_stategif)

                if strategy == "BOB" or strategy == "inter2":
                    stategif = state(
                        evader_probability  = evader_probabilities,
                        teammate_probability= teammate_probabilities,
                        teammate_evader_probability = teammate_evader_probabilities,
                        teammate_teammate_probability= teammate_teammate_probabilities, 
                        agent_position      = agent_position)
                else:
                    stategif = state(
                        evader_probability  = evader_probabilities,
                        teammate_probability= teammate_probabilities,
                        agent_position      = agent_position)
                p1_state_vector.append(stategif)

                if len(p1_state_vector) > 1:
                    p2_state_vector.append(p2_state_vector[-1])
                    e1_state_vector.append(e1_state_vector[-1])
                

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
                p2_results = knowledge_based_action("P2", p2_running_games, p2_dqn, epsilon, [None]*len(p2_running_indexes), p2_first_knowledge_model, False, [steps[i] / (2 * t_max) for i in p2_running_indexes])
            else:
                p2_results = []
        else:
            p2_results = []
        
        evader_running_index = []

        for index, running_index in enumerate(p2_running_indexes):
            if strategy == "BOB":
                (agent_position, 
                 action, 
                 p2_first_knowledge_states[running_index],
                 evader_probabilities, 
                 teammate_probabilities, 
                 p2_second_knowledge_states[running_index],
                 teammate_evader_probabilities, 
                 teammate_teammate_probabilities, 
                 )  = p2_results[index]
            elif strategy == "FIRST":
                (agent_position, 
                action, 
                evader_probabilities, 
                teammate_probabilities, 
                p2_first_knowledge_states[running_index]
                ) = p2_results[index]
            elif strategy == "KBU":
                (agent_position, 
                action, 
                evader_probabilities, 
                teammate_probabilities, 
                _,
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


                    action = ia2(evader_probabilities.cpu().numpy(), teammate_probabilities.cpu().numpy(), agent_position, (steps[running_index]  / (2 * t_max)), 0.1, 15, valid_moves)  
                elif strategy == "interKBU":
                    agent_position                  = games[running_index].agents["P2"].position
                    valid_moves                     = games[running_index].valid_moves(agent_position)  
                    evader_probabilities, teammate_probabilities = p2_first_knowledge_model.forward("P2", games[running_index]) 

                    action = ia2_KBU(evader_probabilities, teammate_probabilities, agent_position, (steps[running_index]  / (2 * t_max)), 0.1, 15, valid_moves)
                elif strategy == "inter2":
                    time_left = (steps[running_index]  / (2 * t_max))
                    agent_position                  = games[running_index].agents["P2"].position
                    valid_moves                     = games[running_index].valid_moves(agent_position)  
                    hidden_state_0 = p2_first_knowledge_states[running_index][0].squeeze(0)
                    cell_state_0   = p2_first_knowledge_states[running_index][1].squeeze(0)

                    second_hidden_state_0 = p2_second_knowledge_states[running_index][0].squeeze(0)
                    second_cell_state_0   = p2_second_knowledge_states[running_index][1].squeeze(0)

                    observation, observed_action = get_observation("P2", games[running_index], delete_observed_actions_since_last_turn_array=True, get_action=True)
                    hidden_state_1, cell_state_1, evader_logits, teammate_logits = p2_first_knowledge_model(observation, hidden_state_0, cell_state_0)
                    second_hidden_state_1, second_cell_state_1, second_evader_logit, second_teammate_logit = p2_second_knowledge_model(
                        observation.unsqueeze(0), observed_action.unsqueeze(0), 
                        evader_logits.unsqueeze(0), teammate_logits.unsqueeze(0), 
                        hidden_state_1.unsqueeze(0), cell_state_1.unsqueeze(0), 
                        second_hidden_state_0.unsqueeze(0), second_cell_state_0.unsqueeze(0), 
                        [time_left])


                    p2_first_knowledge_states[running_index] = (hidden_state_1, cell_state_1)
                    p2_second_knowledge_states[running_index] = (second_hidden_state_1, second_cell_state_1)

                    evader_probabilities    = torch.softmax(evader_logits, dim=0)
                    teammate_probabilities  = torch.softmax(teammate_logits, dim=0)

                    teammate_evader_probabilities    = torch.softmax(second_evader_logit.squeeze(0), dim=0)
                    teammate_teammate_probabilities  = torch.softmax(second_teammate_logit.squeeze(0), dim=0)

                    action = ia2_2nd(evader_probabilities.cpu().numpy(), teammate_probabilities.cpu().numpy(), 
                                     teammate_evader_probabilities.cpu().numpy(), teammate_teammate_probabilities.cpu().numpy(), 
                                     agent_position, time_left, 0.1, 15, valid_moves)

                else:
                    agent_position      = games[running_index].agents["P2"].position
                    valid_moves = games[running_index].valid_moves(agent_position)
                    best_action = valid_moves[0]
                    best_dist   = float("inf")
                    best_longest = float("inf")
                    for act in valid_moves:
                        new_position = games[running_index].new_position(agent_position, act)
                        new_dist, x_dist, y_dist     = manhattan(new_position, games[running_index].agents["E1"].position, True)
                        longest = max(x_dist, y_dist)
                        if new_dist <= best_dist and best_longest > longest:
                            best_dist = new_dist
                            best_action = act
                    action = best_action

            if make_gif:
                if strategy == "BOB" or strategy == "inter2":
                    stategif = state(
                        evader_probability  = evader_probabilities,
                        teammate_probability= teammate_probabilities,
                        teammate_evader_probability = teammate_evader_probabilities,
                        teammate_teammate_probability= teammate_teammate_probabilities, 
                        agent_position      = agent_position)
                else:
                    stategif = state(
                        evader_probability  = evader_probabilities,
                        teammate_probability= teammate_probabilities,
                        agent_position      = agent_position)
                
                p1_state_vector.append(p1_state_vector[-1])
                p2_state_vector.append(stategif)
                e1_state_vector.append(e1_state_vector[-1])

            steps[running_index] += 1
            games[running_index].agent_move("P2", action)
            captured[running_index] = games[running_index].is_evader_captured()

            if captured[running_index] or steps[running_index] >= 2 * t_max :
                terminal_helper(running_index)
            else:
                evader_running_index.append(running_index)
        for index in evader_running_index:
            game = games[index]
            
            if make_gif:
                stategif = state(
                                agent_position      = game.agents["E1"].position)
                p1_state_vector.append(p1_state_vector[-1])
                p2_state_vector.append(p2_state_vector[-1])
                e1_state_vector.append(stategif)

            game.agent_move("E1", random.choice(game.valid_moves(game.agents["E1"].position)))
            captured[index] = games[index].is_evader_captured()
            if captured[index] or steps[index] >= 2 * t_max :
                terminal_helper(index)
            

    return 1


if __name__ == "__main__":
    #validate("KBU")
    #validate("BOB")
    #validate("FIRST")
    #validate("naive")
    #validate("inter")
    #validate("inter2")
    #validate("interKBU")
    #validate("KBU")

    #print("\nplots:\n")
    print("Naive is Plottin")
    validate("naive", True)

    print("DQNs are Plottin")
    validate("BOB", True)
    validate("FIRST", True)
    validate("KBU", True)

    print("Trees are Plottin")
    validate("inter", True)
    validate("inter2", True)
    validate("interKBU", True)