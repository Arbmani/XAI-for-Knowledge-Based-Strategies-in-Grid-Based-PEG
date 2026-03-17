import torch
import random 
from environment import Action_to_Index

device = torch.device("cuda")


def get_observation(agent_id, game, delete_observed_actions_since_last_turn_array = True):
    visible_positions, observed_actions = game.observe(agent_id, delete_observed_actions_since_last_turn_array)
    
    agent_position      = game.agents[agent_id].position
    evader_position     = visible_positions.get(game.evader_id, None)

    teammate_id         = game.pursuer_ids[0] if agent_id == game.pursuer_ids[1] else game.pursuer_ids[1]
    teammate_position   = visible_positions.get(teammate_id, None)

    for(observed_id, _, position) in observed_actions:
        if observed_id == teammate_id:
            teammate_position = position
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
    return observation

def knowledge_based_action(agent_id, game, dqn, epsilon, state, knowledge_model, lstm):
    agent_position  = game.agents[agent_id].position
    valid           = game.valid_moves(agent_position)
        
    if lstm == False:
        evader_probabilities, teammate_probabilities = knowledge_model.forward(agent_id, game) 
        evader_probabilities    = torch.tensor(evader_probabilities, dtype=torch.float32, device=device).unsqueeze(0)
        teammate_probabilities  = torch.tensor(teammate_probabilities, dtype=torch.float32, device=device).unsqueeze(0)
    else:
        observation     = get_observation(agent_id, game, delete_observed_actions_since_last_turn_array=True)
        hidden_state_0, cell_state_0  = state
        hidden_state_1, cell_state_1, evader_logits, teammate_logits = knowledge_model(observation.unsqueeze(0), hidden_state_0, cell_state_0)
        state = hidden_state_1, cell_state_1
        evader_probabilities    = torch.log_softmax(evader_logits, dim=1)
        teammate_probabilities  = torch.log_softmax(teammate_logits, dim=1)

    q = dqn(evader_probabilities, teammate_probabilities, agent_position)

    if random.random() < epsilon:
        action = random.choice(valid)
    else:
        best_action = valid[0]
        best_value  = float("-inf")

        for action in valid:
            value = q[0, Action_to_Index[action]].item()
            if value > best_value:
                best_value  = value
                best_action = action
        action = best_action

    return agent_position, action, evader_probabilities[0].detach().cpu().numpy(), teammate_probabilities[0].detach().cpu().numpy(), state


