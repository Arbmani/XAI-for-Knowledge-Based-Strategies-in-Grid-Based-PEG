from action import device, knowledge_based_action_bob_dqn, knowledge_based_action
import torch
import numpy as np
import random 
from environment import Action_to_Index, Create_Game, Index_to_Action
from dataclasses import dataclass
from sklearn.tree import DecisionTreeClassifier
import json


from LSTM       import LSTM
from LSTM_BOB   import LSTM_BOB

from KBU        import KBU
from DQN        import DQN
from DQN_BOB    import DQN_BOB

def get_feature_names(tree_input_names):
    interpretable_combination_names = [f"{tree_input_names[i]} - {tree_input_names[j]}" for i in range(len(tree_input_names)) for j in range(i + 1, len(tree_input_names))]
    return tree_input_names + interpretable_combination_names

def get_feature_vector(tree_input):
    combinations = [tree_input[i] - tree_input[j] for i in range(len(tree_input)) for j in range(i + 1, len(tree_input))]
    return np.concatenate([tree_input, combinations])

def get_feature_matrix(tree_input_dataset):
    combinations = [tree_input_dataset[:,i] - tree_input_dataset[:,j] for i in range(tree_input_dataset.shape[1]) for j in range(i + 1, tree_input_dataset.shape[1])]
    return np.column_stack([tree_input_dataset] + combinations)



def symbolic_representation(evader_probabilities, teammate_probabilities, teammate_evader_probability, teammate_teammate_probability, agent_positions, time_left, gamma, size):
    def map_to_mass(probabilities):
        probabilities = probabilities.reshape(size, size)
        agent_row, agent_column = agent_positions

        meshgrid_rows, meshgrid_columns = np.meshgrid(
            np.arange(size),
            np.arange(size),
        )

        Laplaceian_Kernel = np.exp(-(gamma * np.sqrt((meshgrid_rows - agent_row)**2 + (meshgrid_columns - agent_column)**2)))

        probabilities_UP    = np.sum(probabilities * Laplaceian_Kernel * (agent_row        >   meshgrid_rows)) 
        probabilities_DOWN  = np.sum(probabilities * Laplaceian_Kernel * (agent_row        <   meshgrid_rows))
        probabilities_LEFT  = np.sum(probabilities * Laplaceian_Kernel * (agent_column     >   meshgrid_columns))
        probabilities_RIGHT = np.sum(probabilities * Laplaceian_Kernel * (agent_column     <   meshgrid_columns))
        
        return np.array([probabilities_UP, probabilities_DOWN, probabilities_LEFT, probabilities_RIGHT], dtype=np.float32)

    evader_masses   = map_to_mass(evader_probabilities)
    teammate_masses = map_to_mass(teammate_probabilities)
    if teammate_evader_probability is not None:
        teammate_evader_masses   = map_to_mass(teammate_evader_probability)
        teammate_teammate_masses = map_to_mass(teammate_teammate_probability)
        return np.concatenate([evader_masses, teammate_masses, teammate_evader_masses, teammate_teammate_masses, agent_positions, [time_left]])
    return np.concatenate([evader_masses, teammate_masses, agent_positions, [time_left]])

def get_training_data(agent_id, game, dqn, knowledge_states, knowledge_model, knowledge_states2nd, knowledge_model2nd, gamma, size, time_left, strategy):
    epsilon = 0
    q_values_bool                   = True
    teammate_evader_probability     = None
    teammate_teammate_probability   = None 
    if strategy == "First_Order_KBU_DT":
        lstm                            = False
        knowledge_states2nd             = None
        results = knowledge_based_action(agent_id, [game], dqn, epsilon, [knowledge_states], knowledge_model, lstm, [time_left], q_values_bool)
        (agent_position, 
        action, 
        evader_probability, 
        teammate_probability, 
        knowledge_states,
        q_values,
        valid_actions
        ) = results[0]
        knowledge_states2nd             = None
    elif strategy == "First_Order_BBU_DT":
        lstm                            = True
        knowledge_states2nd             = None
        results = knowledge_based_action(agent_id, [game], dqn, epsilon, [knowledge_states], knowledge_model, lstm, [time_left], q_values_bool)
        (agent_position, 
        action, 
        evader_probability, 
        teammate_probability, 
        knowledge_states,
        q_values,
        valid_actions
        ) = results[0]

    elif strategy == "Second_Order_BBU_DT":
        results = knowledge_based_action_bob_dqn(
            agent_id, [game], dqn, epsilon, [knowledge_states], [knowledge_states2nd], knowledge_model, knowledge_model2nd, [time_left], q_values_bool)

        (agent_position, 
        action, 
        knowledge_states,
        evader_probability, 
        teammate_probability, 
        knowledge_states2nd,
        teammate_evader_probability,
        teammate_teammate_probability,
        q_values,
        valid_actions
        ) = results[0]
    else:
        raise Exception("Illegal strategy specified")
    oracle_weight = np.mean(q_values - np.min(q_values))

    action = Action_to_Index[action]
    valid_actions = [Action_to_Index[act] for act in valid_actions]

    input_representation = symbolic_representation(evader_probability, teammate_probability, teammate_evader_probability, teammate_teammate_probability, agent_position, time_left, gamma, size)
    return Training_Data(
        symbolic_input_representation   =   input_representation,
        oracle_q_values                 =   q_values,
        agent_position                  =   agent_position,
        oracle_action                   =   action,
        oracle_action_weight            =   oracle_weight,
        valid_actions                   =   valid_actions), knowledge_states, knowledge_states2nd


@dataclass
class Training_Data:
    symbolic_input_representation   : np.ndarray
    oracle_q_values                 : np.ndarray
    agent_position                  : np.ndarray
    oracle_action                   : int 
    oracle_action_weight            : float
    valid_actions                   : list[int]


def symbolic_based_action(tree, symbolic_input_representation, valid_actions):
    feature_vector = get_feature_vector(symbolic_input_representation)
    action = tree.predict(feature_vector.reshape(1, -1))[0]
    if action in valid_actions:
        return action
    else:
        return random.choice(valid_actions)







def simulate(agent_id, control_switch, tree_network, 
             p1_oracle_network, p1_knowledge_update, p1_second_knowledge_model,
             p2_oracle_network, p2_knowledge_update, p2_second_knowledge_model,
             size, t_max, seed, gamma, strategy):

    steps   = 0
    capture = False

    step_cost               = -0.15

    capture_bonus           =  5
    no_capture_loss         = -8

    total_actions           = 0
    action_agreement        = 0


    data_set = []
    game = Create_Game(size=size, t_max=t_max, seed=seed)
    
    p1_states = p1_knowledge_update.init_state()
    p2_states = p2_knowledge_update.init_state()
    if strategy == "Second_Order_BBU_DT":
        p1_states2nd = p1_second_knowledge_model.init_state()
        p2_states2nd = p2_second_knowledge_model.init_state()
    else:
        p1_states2nd = None
        p2_states2nd = None

    reward = 0
    for t in range(t_max):

        p1_data, p1_states, p1_states2nd = get_training_data("P1", game, p1_oracle_network, p1_states, p1_knowledge_update, p1_states2nd, p1_second_knowledge_model, gamma, size, (steps / (2 * t_max)), strategy)

        if agent_id == "P1":
            data_set.append(p1_data)
        if agent_id == "P1" and control_switch:
            p1_action = symbolic_based_action(tree_network, p1_data.symbolic_input_representation, p1_data.valid_actions)
            total_actions += 1
            if p1_action == p1_data.oracle_action:
                action_agreement += 1
        else:
            p1_action = p1_data.oracle_action
        game.agent_move("P1", Index_to_Action[p1_action])
        steps += 1 
        if game.is_evader_captured():
            capture = True
            break
        p2_data, p2_states, p2_states2nd = get_training_data("P2", game, p2_oracle_network, p2_states, p2_knowledge_update, p2_states2nd,  p2_second_knowledge_model, gamma, size, (steps / (2 * t_max)), strategy)

        if agent_id == "P2":
            data_set.append(p2_data)
        if agent_id == "P2" and control_switch:
            p2_action = symbolic_based_action(tree_network, p2_data.symbolic_input_representation, p2_data.valid_actions)
            total_actions += 1
            if p2_action == p2_data.oracle_action:
                action_agreement += 1
        else:
            p2_action = p2_data.oracle_action
        game.agent_move("P2", Index_to_Action[p2_action])
        steps += 1 
        if game.is_evader_captured():
            capture = True
            break
        game.agent_move("E1", random.choice(game.valid_moves(game.agents["E1"].position)))
        if game.is_evader_captured():
            capture = True
            break

        reward += step_cost
    if capture:
        reward += capture_bonus 
    else:
        reward += no_capture_loss


    return data_set, reward, capture, steps, action_agreement, total_actions


def collect_dataset(agent_id, control_switch, tree_network, 
                    p1_oracle_network, p1_knowledge_update, p1_second_knowledge_model,
                    p2_oracle_network, p2_knowledge_update, p2_second_knowledge_model,
                    size, t_max, seed, gamma, dataset_size, strategy):

    symbolic_input_representations  = []        
    oracle_actions                  = []       
    oracle_action_weights           = []

    simulate_seed = seed

    while(len(symbolic_input_representations)) < dataset_size:
        states, _, _, _,_,_ = simulate(agent_id, control_switch, tree_network, 
                                        p1_oracle_network, p1_knowledge_update, p1_second_knowledge_model,
                                        p2_oracle_network, p2_knowledge_update, p2_second_knowledge_model,
                                        size, t_max, simulate_seed, gamma, strategy)
        simulate_seed += 1

        for state in states:
            if len(symbolic_input_representations) >= dataset_size:
                break
            symbolic_input_representations.append(state.symbolic_input_representation)
            oracle_actions.append(state.oracle_action)
            oracle_action_weights.append(state.oracle_action_weight)

    return (
        np.stack(symbolic_input_representations).astype(np.float32),
        np.asarray(oracle_actions, dtype=np.int64),
        np.asarray(oracle_action_weights, dtype=np.float32),
        )

def validate_tree(agent_id, tree_network, 
                    p1_oracle_network, p1_knowledge_update, p1_second_knowledge_model,
                    p2_oracle_network, p2_knowledge_update, p2_second_knowledge_model,
                    size, t_max, seed, gamma, episodes, save_validation, save_size, strategy):

    rewards     = []
    captures    = []
    steps       = []

    action_agreements   = []
    total_actionss      = []

    simulate_seed = seed 
    for episode in range(episodes):
        _, reward, capture, step, action_agreement, total_actions = simulate(agent_id, True, tree_network, 
                                p1_oracle_network, p1_knowledge_update, p1_second_knowledge_model,
                                p2_oracle_network, p2_knowledge_update, p2_second_knowledge_model,
                                size, t_max, simulate_seed, gamma, strategy)
        simulate_seed += 1
        rewards.append(reward)
        captures.append(capture)
        steps.append(step)
        if total_actions != 0:
            action_agreements.append(action_agreement)
            total_actionss.append(total_actions)

    if save_validation:
        row_results = {
                "Tree Size"             : save_size,
                "Number of Validation"  : episodes, 
                "Steps"                 : np.mean(steps),
                "Captured"              : np.mean(captures),
                "Rewards"               : np.mean(rewards),
                "Action Agreement"      : np.mean(np.array(action_agreements) / np.array(total_actionss)),
                }
        with open(f"Results_Tree_2nd_{save_size}.jsonl", "a") as file:
            file.write(json.dumps(row_results) + "\n")
    return np.mean(rewards), np.mean(captures), np.mean(steps), np.mean(np.array(action_agreements) / np.array(total_actionss))

def save_tree_as_python(Decision_Tree_Classifier, feature_names, agent_id, strategy, max_leaf_nodes):
    tree = Decision_Tree_Classifier.tree_

    index_to_action_string = {
        0 : "WALK LEFT",
        1 : "WALK RIGHT",
        2 : "WALK DOWN",
        3 : "WALK UP",
    }

    def DepthFirstSearch(node_id, depth):
        number_of_tabs = "    "*depth

        if tree.children_left[node_id] == tree.children_right[node_id]: # Leaf
            action = np.argmax(tree.value[node_id][0])
            return f"{number_of_tabs}return {action} # {index_to_action_string[action]}", action 
        
        left_subtree, left_action = DepthFirstSearch(tree.children_left[node_id], depth+1)
        right_subtree, right_action = DepthFirstSearch(tree.children_right[node_id], depth+1)

        if left_action != -1 and right_action != -1 and left_action == right_action:
            return f"{number_of_tabs}return {left_action}", left_action
        
        if_feature      = feature_names[tree.feature[node_id]]
        if_threshold    = tree.threshold[node_id]

        string_tree = (
            f'{number_of_tabs}if features["{if_feature}"] <= {if_threshold:.6f}:\n'
            f"{left_subtree}\n"
            f"{number_of_tabs}else:\n"
            f"{right_subtree}"
        )
        return string_tree, -1
    
    string_tree, _ = DepthFirstSearch(0, 1)

    python_program = (
        "import random\n"
        "from INTERPRETER import symbolic_representation, get_feature_vector\n"
        "from environment import Index_to_Action\n"
        f"symbol_names = {str(feature_names)}\n"
        "\n\n"
        "def interpretable_strategy(features):\n"
        f"{string_tree}\n"
        "\n\n"
        "def interpretable_action(Evader_Probability_Grid, Teammate_Probability_Grid, Teammate_Evader_Probability_Grid, Teammate_Teammate_Probability_Grid, Main_Agent_Position, Time_Left, Gamma, Size, Valid_Actions):\n"
        "    input_representation = symbolic_representation(Evader_Probability_Grid, Teammate_Probability_Grid, Teammate_Evader_Probability_Grid, Teammate_Teammate_Probability_Grid, Main_Agent_Position, Time_Left, Gamma, Size)\n"
        "    input_combinations   = get_feature_vector(input_representation)\n"
        "    symbol_to_value     = {name: input_combinations[i] for i, name in enumerate(symbol_names)}\n"
        "    action               = Index_to_Action[interpretable_strategy(symbol_to_value)]\n"
        "    if action in Valid_Actions:\n"
        "        return action\n"
        "    else:\n"
        "        return random.choice(Valid_Actions)\n"
    )


    with open(f"Decision_Trees/{strategy}/{agent_id}_{max_leaf_nodes}.py", "w") as file:
        file.write(python_program)



        
    return

def interpreter(agent_id, size,
                p1_oracle_network, p1_knowledge_update, p1_second_knowledge_model,
                p2_oracle_network, p2_knowledge_update, p2_second_knowledge_model,
                max_leaf_nodes, strategy):
    
    if strategy == "Second_Order_BBU_DT":
        names = [
            "Evader(UP)", "Evader(DOWN)", "Evader(LEFT)", "Evader(RIGHT)",
            "Teammate(UP)", "Teammate(DOWN)", "Teammate(LEFT)", "Teammate(RIGHT)",
            "Teammate(Evader(UP))", "Teammate(Evader(DOWN))", "Teammate(Evader(LEFT))", "Teammate(Evader(RIGHT))",
            "Teammate(Teammate(UP))", "Teammate(Teammate(DOWN))", "Teammate(Teammate(LEFT))", "Teammate(Teammate(RIGHT))",
            "Agent_Row", "Agent_Column", "Time_Left"
            ]
    else:
        names = [
            "Evader(UP)", "Evader(DOWN)", "Evader(LEFT)", "Evader(RIGHT)",
            "Teammate(UP)", "Teammate(DOWN)", "Teammate(LEFT)", "Teammate(RIGHT)",
            "Agent_Row", "Agent_Column", "Time_Left"
            ]

    feature_names = get_feature_names(names)
    
    number_of_trees = 10
    features = None
    t_max   = 50
    seed    = 1

    tree_network = None
    gamma        = 0.1
    
    dataset_size = 100_000
    episodes     = 5_000
    best_score = float("-inf")
    best_tree  = None
    for tree_index in range(number_of_trees):
        seed = seed + dataset_size
        control_switch = False if tree_index == 0 else True

        symbolic_input_representation, oracle_action, oracle_action_weight = collect_dataset(
            agent_id, control_switch, tree_network, 
            p1_oracle_network, p1_knowledge_update, p1_second_knowledge_model,
            p2_oracle_network, p2_knowledge_update, p2_second_knowledge_model,
            size, t_max, seed, gamma, dataset_size, strategy)
        
        if features is None:
            concatenate_oracle_actions              = oracle_action
            concatenate_oracle_action_weights       = oracle_action_weight
            features                                = get_feature_matrix(symbolic_input_representation)
        else:
            concatenate_oracle_actions              = np.concatenate([concatenate_oracle_actions, oracle_action])
            concatenate_oracle_action_weights       = np.concatenate([concatenate_oracle_action_weights, oracle_action_weight])
            features                                = np.vstack([features, get_feature_matrix(symbolic_input_representation)])


        tree_network = DecisionTreeClassifier(
            max_leaf_nodes=max_leaf_nodes,
            random_state=seed,
        )
        tree_network.fit(features, concatenate_oracle_actions, sample_weight=concatenate_oracle_action_weights)
        mean_rewards, mean_captures, mean_steps, mean_action_agreement = validate_tree(
                agent_id, tree_network, 
                p1_oracle_network, p1_knowledge_update, p1_second_knowledge_model,
                p2_oracle_network, p2_knowledge_update, p2_second_knowledge_model,
                size, t_max, seed + (dataset_size * number_of_trees * 2), gamma, episodes, False, max_leaf_nodes, strategy)

        print(f"For agent {agent_id}, "
            f"tree index {tree_index}, "
            f"Mean rewards {mean_rewards}, "
            f"Mean captures {mean_captures}, "
            f"Mean steps {mean_steps}.",
            f"Mean action agreement {mean_action_agreement}")


        if mean_rewards > best_score:
            best_score  = mean_rewards
            best_tree   = tree_network
        
        

    #val_mean_rewards, val_mean_captures, val_mean_steps, val_mean_action_agreement = validate_tree(
    #            agent_id, best_tree, 
    #            p1_oracle_network, p1_knowledge_update, p1_second_knowledge_model,
    #            p2_oracle_network, p2_knowledge_update, p2_second_knowledge_model,
    #            size, t_max, 109133331, gamma, 40_000, True, max_leaf_nodes, strategy)
    

    #print("     Validation Results:")
    #print(f"        For agent {agent_id}, "
    #    f"tree index {tree_index}, "
    #    f"Mean rewards {val_mean_rewards}, "
    #    f"Mean captures {val_mean_captures}, "
    #    f"Mean steps {val_mean_steps}.",
    #    f"Mean action agreement {val_mean_action_agreement}")

    save_tree_as_python(best_tree, feature_names, agent_id, strategy, max_leaf_nodes)


    return



def distill(strategy):
    size = 15
    possible_positions = size*size 

    p1_second_knowledge_model = None
    p2_second_knowledge_model = None
    if strategy == "First_Order_KBU_DT":
        p1_first_knowledge_model = KBU(size)
        p2_first_knowledge_model = KBU(size) 

        p1_dqn = DQN(possible_positions, device).to(device)
        p1_dqn.load_state_dict(torch.load(f"PyTorch_Models/p1_dqn_kbu.pt", map_location = device))
        p2_dqn = DQN(possible_positions, device).to(device)
        p2_dqn.load_state_dict(torch.load(f"PyTorch_Models/p2_dqn_kbu.pt", map_location = device))

    elif strategy == "First_Order_BBU_DT":
        p1_first_knowledge_model = LSTM(hidden_state_size = 256, possible_positions = possible_positions, device=device).to(device)
        p1_first_knowledge_model.load_state_dict(torch.load(f"PyTorch_Models/p1_lstm256.pt", map_location = device))
        p1_first_knowledge_model.stop()

        p2_first_knowledge_model = LSTM(hidden_state_size = 256, possible_positions = possible_positions, device=device).to(device)
        p2_first_knowledge_model.load_state_dict(torch.load(f"PyTorch_Models/p2_lstm256.pt", map_location = device))
        p2_first_knowledge_model.stop()


        p1_dqn = DQN(possible_positions, device).to(device)
        p1_dqn.load_state_dict(torch.load("p1_dqn_lstm.pt", map_location=device))
        p1_dqn.stop()

        p2_dqn = DQN(possible_positions, device).to(device)
        p2_dqn.load_state_dict(torch.load("p2_dqn_lstm.pt", map_location=device))
        p2_dqn.stop()


    elif strategy == "Second_Order_BBU_DT":
        p1_first_knowledge_model = LSTM(hidden_state_size = 256, possible_positions = possible_positions, device=device).to(device)
        p1_first_knowledge_model.load_state_dict(torch.load(f"PyTorch_Models/p1_lstm256.pt", map_location = device))

        p1_second_knowledge_model = LSTM_BOB(first_hidden_state_size = 256, hidden_state_size = 512, possible_positions = possible_positions, device=device).to(device)
        p1_second_knowledge_model.load_state_dict(torch.load(f"PyTorch_Models/p1_lstm_2nd.pt", map_location = device))

        p1_first_knowledge_model.stop()
        p1_second_knowledge_model.stop()


        p2_first_knowledge_model = LSTM(hidden_state_size = 256, possible_positions = possible_positions, device=device).to(device)
        p2_first_knowledge_model.load_state_dict(torch.load(f"PyTorch_Models/p2_lstm256.pt", map_location = device))

        p2_second_knowledge_model = LSTM_BOB(first_hidden_state_size = 256, hidden_state_size = 512, possible_positions = possible_positions, device=device).to(device)
        p2_second_knowledge_model.load_state_dict(torch.load(f"PyTorch_Models/p2_lstm_2nd.pt", map_location = device))

        p2_first_knowledge_model.stop()
        p2_second_knowledge_model.stop()


        p1_dqn = DQN_BOB(possible_positions, device).to(device)
        p1_dqn.load_state_dict(torch.load(f"PyTorch_Models/p1_dqn_boblstm.pt", map_location = device))
        p1_dqn.eval()

        p2_dqn = DQN_BOB(possible_positions, device).to(device)
        p2_dqn.load_state_dict(torch.load(f"PyTorch_Models/p2_dqn_boblstm.pt", map_location = device))
        p2_dqn.eval()
    max_leaf_nodes = [512]
    for max_leaf_node in max_leaf_nodes:
        interpreter("P1", size, 
                    p1_dqn, p1_first_knowledge_model, p1_second_knowledge_model, 
                    p2_dqn, p2_first_knowledge_model, p2_second_knowledge_model,
                    max_leaf_node, strategy)

        interpreter("P2", size, 
                    p1_dqn, p1_first_knowledge_model, p1_second_knowledge_model, 
                    p2_dqn, p2_first_knowledge_model, p2_second_knowledge_model,
                    max_leaf_node, strategy)

if __name__ == "__main__":

    #distill("First_Order_KBU_DT")
    #distill("First_Order_BBU_DT")
    distill("Second_Order_BBU_DT")



    