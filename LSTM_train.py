import random 
import torch

from action import get_observation, device 
from environment import Create_Game
from LSTM import LSTM 

def simulate(game, size, t_max):

    P1_observations = []
    P2_observations = []

    P1_positions    = []
    P2_positions    = []
    E1_positions    = []

    def row_col_to_scalar(position):
        row, col = position
        return row * size + col 
    
    for t in range(t_max):
        P1_observations.append(get_observation("P1", game))
        P2_observations.append(get_observation("P2", game))

        P1_positions.append(row_col_to_scalar(game.agents["P1"].position))
        P2_positions.append(row_col_to_scalar(game.agents["P2"].position))
        E1_positions.append(row_col_to_scalar(game.agents["E1"].position))

        game.agent_move("P1", random.choice(game.valid_moves(game.agents["P1"].position)))
        if game.is_evader_captured():
            break
        game.agent_move("P2", random.choice(game.valid_moves(game.agents["P2"].position)))
        if game.is_evader_captured():
            break 
        game.agent_move("E1", random.choice(game.valid_moves(game.agents["E1"].position)))
        if game.is_evader_captured():
            break 
    return P1_observations, P2_observations, P1_positions, P2_positions, E1_positions

def batch(size, batch_size, t_max, seed):
    P1_observations_batch = []
    P2_observations_batch = []

    P1_positions_batch    = []
    P2_positions_batch    = []
    E1_positions_batch    = []

    for simulation in range(batch_size):
        game = Create_Game(size, t_max, seed+simulation)

        P1_observations, P2_observations, P1_positions, P2_positions, E1_positions = simulate(game, size, t_max)

        P1_observations_batch.append(P1_observations)
        P2_observations_batch.append(P2_observations)

        P1_positions_batch.append(P1_positions)
        P2_positions_batch.append(P2_positions)
        E1_positions_batch.append(E1_positions)

    P1_observations_batch_tensor    = torch.zeros(batch_size, t_max, 8, dtype=torch.float32)
    P2_observations_batch_tensor    = torch.zeros(batch_size, t_max, 8, dtype=torch.float32)
    P1_positions_batch_tensor       = torch.zeros(batch_size, t_max, dtype=torch.float32)
    P2_positions_batch_tensor       = torch.zeros(batch_size, t_max, dtype=torch.float32)
    E1_positions_batch_tensor       = torch.zeros(batch_size, t_max, dtype=torch.float32)
    mask_tensor                     = torch.zeros(batch_size, t_max, dtype=torch.float32)

    for batch in range(batch_size):
        T = len(P1_observations_batch[batch])

        P1_observations_batch_tensor[batch, : T] = torch.stack(P1_observations_batch[batch], dim = 0)
        P2_observations_batch_tensor[batch, : T] = torch.stack(P2_observations_batch[batch], dim = 0)

        P1_positions_batch_tensor[batch, :T]    = torch.stack(P1_positions_batch[batch], dyupe=torch.float32)
        P2_positions_batch_tensor[batch, :T]    = torch.stack(P2_positions_batch[batch], dyupe=torch.float32)
        E1_positions_batch_tensor[batch, :T]    = torch.stack(E1_positions_batch[batch], dyupe=torch.float32)

        mask_tensor[batch, :T]                  = 1.0

    return (P1_observations_batch_tensor.to(device),
            P2_observations_batch_tensor.to(device),
            P1_positions_batch_tensor.to(device),
            P2_positions_batch_tensor.to(device),
            E1_positions_batch_tensor.to(device),
            mask_tensor.to(device))


def loss(lstm, observations, evader_positions, teamamte_positions, mask):
    return -1

if __name__ == "__main__":
    size = 15
    t_max = 50
    hidden_state_sizes = [32, 64, 128, 256]
    updates = 2000
    batch_size = 64
    learning_rate = 1e-3
    possible_positions = size*size 
    seed  =1

    for hidden_state_size in hidden_state_sizes:
        random.seed(seed)
        torch.manual_seed(seed)

        p1_lstm = LSTM(8, hidden_state_size, possible_positions, device).to(device)
        p2_lstm = LSTM(8, hidden_state_size, possible_positions, device).to(device)

        p1_lstm_opt = torch.optim.Adam(p1_lstm.parameters(), lr=learning_rate)
        p2_lstm_opt = torch.optim.Adam(p2_lstm.parameters(), lr=learning_rate)

        for update in range(updates):
            seed = seed + update 
            (P1_observations_batch_tensor,
            P2_observations_batch_tensor,
            P1_positions_batch_tensor,
            P2_positions_batch_tensor,
            E1_positions_batch_tensor,
            mask_tensor) = batch(size, batch_size, t_max, seed)

            









