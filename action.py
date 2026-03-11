import torch
import random 
from dataclasses import dataclass
from environment import Game, Action_to_Index

device = torch.device("cuda")
@dataclass
class Agent_State:
    hidden_state: torch.Tensor
    cell_state  : torch.Tensor

def get_observation(agent_id, game):
    visible_positions, observed_actions = game.observe(agent_id)
    
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
        [[agent_row, agent_column, evader_observed, evader_row, evader_column, teammate_observed, teammate_row, teammate_column]],
        dtype=torch.float32, 
    )
    return observation

def knowledge_based_action(agent_id, game, dqn, lstm, state, epsilon):
    agent_position  = game.agents[agent_id].position
    valid           = game.valid_moves(agent_position)
        
    observation     = get_observation(agent_id, game)

    hidden_state_0  = state.hidden_state
    cell_state_0    = state.cell_state

    state.hidden_state, state.cell_state, evader_logits, teammate_logits = lstm(observation, hidden_state_0, cell_state_0)
    
    q = dqn(evader_logits, teammate_logits, agent_position)

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

    return action, q, evader_logits, teammate_logits, observation, agent_position, valid,  hidden_state_0, cell_state_0



