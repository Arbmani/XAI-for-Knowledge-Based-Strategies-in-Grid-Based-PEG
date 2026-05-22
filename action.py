import torch
import random 
import numpy as np
from environment import Action_to_Index

device = torch.device("cuda")

def get_observation(agent_id, game, delete_observed_actions_since_last_turn_array = True, get_action = False):
    visible_positions, observed_actions = game.observe(agent_id, delete_observed_actions_since_last_turn_array)
    
    agent_position      = game.agents[agent_id].position
    evader_position     = visible_positions.get(game.evader_id, None)

    teammate_id         = game.pursuer_ids[0] if agent_id == game.pursuer_ids[1] else game.pursuer_ids[1]
    teammate_position   = visible_positions.get(teammate_id, None)

    return_action = None

    for(observed_id, old_position, position) in observed_actions:
        if observed_id == teammate_id:
            teammate_position = position
            if get_action:
                return_action = torch.tensor([1.0, (position[0] - old_position[0]), (position[1] - old_position[1])], device = device, dtype=torch.float32)
        elif observed_id == game.evader_id:
            evader_position = position
    
    evader_observed     = 0 if evader_position is None else 1
    teammate_observed   = 0 if teammate_position is None else 1 

    agent_row, agent_column         = agent_position
    evader_row, evader_column       = (0,0) if evader_position is None else evader_position
    teammate_row, teammate_column   = (0,0) if teammate_position is None else teammate_position

    observation = torch.tensor(
        [agent_row, agent_column, evader_observed, evader_row, evader_column, teammate_observed, teammate_row, teammate_column],
        dtype=torch.float32, 
        device=device,
    )
    if get_action:
        if return_action is None:
            return_action = torch.tensor([0.0, 0.0, 0.0], device=device, dtype=torch.float32)
        return observation, return_action
    return observation

def knowledge_based_action(agent_id, games, dqn, epsilon, states, knowledge_model, lstm, time_left, q_values_bool = False):
    '''
    First-Order DQN Action Selection
    '''
    with torch.no_grad():
        agent_positions             = []
        valid_moves                 = []
        for game in games: 
            agent_position  = game.agents[agent_id].position

            agent_positions.append(agent_position)
            valid_moves.append(game.valid_moves(agent_position))        
        if lstm:
            observation = [get_observation(agent_id, game, delete_observed_actions_since_last_turn_array=True) for game in games]
            observation = torch.stack(observation, dim=0)

            hidden_state_0 = torch.cat([state[0] for state in states], dim=0)
            cell_state_0   = torch.cat([state[1] for state in states], dim=0)

            hidden_state_1, cell_state_1, evader_logits, teammate_logits = knowledge_model(observation, hidden_state_0, cell_state_0)

            for i in range(len(states)):
                states[i] = (hidden_state_1[i:i+1], cell_state_1[i:i+1])

            evader_probabilities    = torch.softmax(evader_logits, dim=1)
            teammate_probabilities  = torch.softmax(teammate_logits, dim=1)

        else:
            evader_probabilities_list = []
            teammate_probabilities_list = []

            for game in games:
                evader_probabilities, teammate_probabilities = knowledge_model.forward(agent_id, game) 
                evader_probabilities_list.append(evader_probabilities)
                teammate_probabilities_list.append(teammate_probabilities)



            evader_probabilities    = torch.tensor(np.stack(evader_probabilities_list), dtype=torch.float32, device=device)
            teammate_probabilities  = torch.tensor(np.stack(teammate_probabilities_list), dtype=torch.float32, device=device)


        q = dqn(evader_probabilities, teammate_probabilities, agent_positions, time_left)


        results = []
        for i in range(len(games)):
            valid = valid_moves[i]
            if random.random() < epsilon:
                action = random.choice(valid)
            else:
                best_action = valid[0]
                best_value  = float("-inf")
                for action in valid:
                    value = q[i, Action_to_Index[action]].item()
                    if value > best_value:
                        best_value  = value
                        best_action = action
                action = best_action
            if q_values_bool:
                results.append((agent_positions[i], action, evader_probabilities[i].cpu().numpy(), teammate_probabilities[i].cpu().numpy(), states[i], q[i].cpu().numpy(),valid))
            else:
                results.append((agent_positions[i], action, evader_probabilities[i].cpu().numpy(), teammate_probabilities[i].cpu().numpy(), states[i] if lstm else None))
        return results



def knowledge_based_action_bob(agent_id, games, dqn, epsilon, states, knowledge_model, time_left):
    '''
        Only used for training the second-order LSTM.
    '''
    with torch.no_grad():
        agent_positions             = []
        valid_moves                 = []
        for game in games: 
            agent_position  = game.agents[agent_id].position

            agent_positions.append(agent_position)
            valid_moves.append(game.valid_moves(agent_position))        

        observation = [get_observation(agent_id, game, delete_observed_actions_since_last_turn_array=True) for game in games]
        observation = torch.stack(observation, dim=0)

        hidden_state_0 = torch.cat([state[0] for state in states], dim=0)
        cell_state_0   = torch.cat([state[1] for state in states], dim=0)

        hidden_state_1, cell_state_1, evader_logits, teammate_logits = knowledge_model(observation, hidden_state_0, cell_state_0)


        evader_probabilities    = torch.softmax(evader_logits, dim=1)
        teammate_probabilities  = torch.softmax(teammate_logits, dim=1)

        q = dqn(evader_probabilities, teammate_probabilities, agent_positions, time_left)
        results = []
        for i in range(len(games)):
            valid = valid_moves[i]
            if random.random() < epsilon:
                action = random.choice(valid)
            else:
                best_action = valid[0]
                best_value  = float("-inf")
                for action in valid:
                    value = q[i, Action_to_Index[action]].item()
                    if value > best_value:
                        best_value  = value
                        best_action = action
                action = best_action
            results.append((action, hidden_state_1[i:i+1], cell_state_1[i:i+1], evader_logits[i], teammate_logits[i], observation[i]))
        return results
  


def knowledge_based_action_bob_dqn(agent_id, games, dqn, epsilon, first_states, second_states, first_knowledge_model, second_knowledge_model, time_left, q_values_bool = False):
    '''
    Second-Order DQN Action Selection
    '''
    with torch.no_grad():
        agent_positions             = []
        valid_moves                 = []
        for game in games: 
            agent_position  = game.agents[agent_id].position

            agent_positions.append(agent_position)
            valid_moves.append(game.valid_moves(agent_position))        


        observation_and_action = [get_observation(agent_id, game, delete_observed_actions_since_last_turn_array=True, get_action=True) for game in games]
        observation, observed_action = zip(*observation_and_action)
        observed_action = torch.stack(observed_action, dim=0)
        observation = torch.stack(observation, dim=0)

        first_hidden_state_0 = torch.cat([state[0] for state in first_states], dim=0)
        first_cell_state_0   = torch.cat([state[1] for state in first_states], dim=0)

        second_hidden_state_0 = torch.cat([state[0] for state in second_states], dim=0)
        second_cell_state_0   = torch.cat([state[1] for state in second_states], dim=0)

        first_hidden_state_1, first_cell_state_1, first_evader_logits, first_teammate_logits = first_knowledge_model(observation, first_hidden_state_0, first_cell_state_0)
        second_hidden_state_1, second_cell_state_1, second_evader_logit, second_teammate_logit = second_knowledge_model(observation, observed_action, first_evader_logits, first_teammate_logits, first_hidden_state_1, first_cell_state_1, second_hidden_state_0, second_cell_state_0, time_left)

        for i in range(len(first_states)):
            first_states[i] = (first_hidden_state_1[i:i+1], first_cell_state_1[i:i+1])
        for i in range(len(second_states)):      
            second_states[i] = (second_hidden_state_1[i:i+1], second_cell_state_1[i:i+1])

        evader_probabilities    = torch.softmax(first_evader_logits, dim=1)
        teammate_probabilities  = torch.softmax(first_teammate_logits, dim=1)
        
        teammate_evader_probabilities    = torch.softmax(second_evader_logit, dim=1)
        teammate_teammate_probabilities  = torch.softmax(second_teammate_logit, dim=1)

        q = dqn(evader_probabilities, teammate_probabilities, teammate_evader_probabilities, teammate_teammate_probabilities, agent_positions, time_left)
        results = []
        for i in range(len(games)):
            valid = valid_moves[i]
            if random.random() < epsilon:
                action = random.choice(valid)
            else:
                best_action = valid[0]
                best_value  = float("-inf")
                for action in valid:
                    value = q[i, Action_to_Index[action]].item()
                    if value > best_value:
                        best_value  = value
                        best_action = action
                action = best_action
            if q_values_bool:
                results.append((agent_positions[i], action, 
                                first_states[i], evader_probabilities[i].cpu().numpy(), teammate_probabilities[i].cpu().numpy(),
                                second_states[i], teammate_evader_probabilities[i].cpu().numpy(), teammate_teammate_probabilities[i].cpu().numpy(), q[i].cpu().numpy(),valid))
            else:
                results.append((agent_positions[i], action, 
                                first_states[i], evader_probabilities[i], teammate_probabilities[i],
                                second_states[i], teammate_evader_probabilities[i], teammate_teammate_probabilities[i]))
        return results