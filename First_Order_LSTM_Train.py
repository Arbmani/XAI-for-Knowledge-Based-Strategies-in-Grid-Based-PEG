import random 
import torch
import torch.nn.functional as F
import numpy as np

from action import get_observation, device 
from environment import Create_Game
from First_Order_LSTM import LSTM 

def simulate(game, size, t_max):

    P1_observations = []
    P2_observations = []

    P1_positions    = []
    P1_positions_P2 = []
    P2_positions    = []
    E1_positions    = []

    def row_col_to_scalar(position):
        row, col = position
        return row * size + col 
    
    for t in range(t_max):
        P1_observations.append(get_observation("P1", game))

        P1_positions.append(row_col_to_scalar(game.agents["P1"].position))
        P2_positions.append(row_col_to_scalar(game.agents["P2"].position))
        E1_positions.append(row_col_to_scalar(game.agents["E1"].position))

        game.agent_move("P1", random.choice(game.valid_moves(game.agents["P1"].position)))
        P2_observations.append(get_observation("P2", game))
        P1_positions_P2.append(row_col_to_scalar(game.agents["P1"].position))
        if game.is_evader_captured():
            break
        game.agent_move("P2", random.choice(game.valid_moves(game.agents["P2"].position)))
        if game.is_evader_captured():
            break 
        game.agent_move("E1", random.choice(game.valid_moves(game.agents["E1"].position)))
        if game.is_evader_captured():
            break 
    return P1_observations, P2_observations, P1_positions, P2_positions, E1_positions, P1_positions_P2

def batch(size, batch_size, t_max, seed):
    P1_observations_batch = []
    P2_observations_batch = []

    P1_positions_batch    = []
    P1_positions_batch_P2 = []
    P2_positions_batch    = []
    E1_positions_batch    = []

    for simulation in range(batch_size):
        game = Create_Game(size, t_max, seed+simulation)

        P1_observations, P2_observations, P1_positions, P2_positions, E1_positions, P1_positions_P2 = simulate(game, size, t_max)

        P1_observations_batch.append(P1_observations)
        P2_observations_batch.append(P2_observations)

        P1_positions_batch.append(P1_positions)
        P1_positions_batch_P2.append(P1_positions_P2)
        P2_positions_batch.append(P2_positions)
        E1_positions_batch.append(E1_positions)

    P1_observations_batch_tensor    = torch.zeros(batch_size, t_max, 8, dtype=torch.float32, device = device)
    P2_observations_batch_tensor    = torch.zeros(batch_size, t_max, 8, dtype=torch.float32, device = device)
    P1_positions_batch_tensor       = torch.zeros(batch_size, t_max, dtype=torch.long, device=device)
    P1_positions_P2_batch_tensor    = torch.zeros(batch_size, t_max, dtype=torch.long, device=device)
    P2_positions_batch_tensor       = torch.zeros(batch_size, t_max, dtype=torch.long, device=device)
    E1_positions_batch_tensor       = torch.zeros(batch_size, t_max, dtype=torch.long, device=device)
    mask_tensor                     = torch.zeros(batch_size, t_max, dtype=torch.float32, device=device)

    for batch in range(batch_size):
        T = len(P1_observations_batch[batch])

        P1_observations_batch_tensor[batch, : T] = torch.stack(P1_observations_batch[batch], dim = 0)
        P2_observations_batch_tensor[batch, : T] = torch.stack(P2_observations_batch[batch], dim = 0)

        P1_positions_P2_batch_tensor[batch, :T] = torch.tensor(P1_positions_batch_P2[batch], dtype=torch.long)
        P1_positions_batch_tensor[batch, :T]    = torch.tensor(P1_positions_batch[batch], dtype=torch.long)
        P2_positions_batch_tensor[batch, :T]    = torch.tensor(P2_positions_batch[batch], dtype=torch.long)
        E1_positions_batch_tensor[batch, :T]    = torch.tensor(E1_positions_batch[batch], dtype=torch.long)

        mask_tensor[batch, :T]                  = 1.0

    return (P1_observations_batch_tensor,
            P2_observations_batch_tensor,
            P1_positions_batch_tensor,
            P2_positions_batch_tensor,
            E1_positions_batch_tensor,
            mask_tensor, P1_positions_P2_batch_tensor)


def loss(p1_lstm, p2_lstm, P1_observations_batch_tensor, P2_observations_batch_tensor, P1_positions_batch_tensor, P2_positions_batch_tensor, E1_positions_batch_tensor, mask_tensor, P1_positions_P2_batch_tensor):

    batch, T, _ = P1_observations_batch_tensor.shape

    p1_hidden_state, p1_cell_state = p1_lstm.init_state(batch)    
    p2_hidden_state, p2_cell_state = p2_lstm.init_state(batch)

    p1_loss = 0.0
    p2_loss = 0.0
    steps   = 0.0

    for t in range(T):
        p1_hidden_state, p1_cell_state, p1_evader_logits, p1_teammate_logits = p1_lstm(P1_observations_batch_tensor[:,t], p1_hidden_state, p1_cell_state)
        p2_hidden_state, p2_cell_state, p2_evader_logits, p2_teammate_logits = p2_lstm(P2_observations_batch_tensor[:,t], p2_hidden_state, p2_cell_state)

        p1_evader_logits_loss       = F.cross_entropy(p1_evader_logits, E1_positions_batch_tensor[:,t], reduction="none")
        p1_teammate_logits_loss     = F.cross_entropy(p1_teammate_logits, P2_positions_batch_tensor[:,t], reduction="none")

        p2_evader_logits_loss       = F.cross_entropy(p2_evader_logits, E1_positions_batch_tensor[:,t], reduction="none")
        p2_teammate_logits_loss     = F.cross_entropy(p2_teammate_logits, P1_positions_P2_batch_tensor[:,t], reduction="none")

        p1_t_loss   = p1_evader_logits_loss + p1_teammate_logits_loss
        p2_t_loss   = p2_evader_logits_loss + p2_teammate_logits_loss

        t_mask      = mask_tensor[:, t]
        p1_loss += (p1_t_loss * t_mask).sum()
        p2_loss += (p2_t_loss * t_mask).sum()

        steps   += t_mask.sum()

    return (p1_loss / steps), (p2_loss / steps)

def validate(p1_lstm, p2_lstm, size, t_max, batch_size, hidden_state_size, batches, seed):

    p1_loss_average = 0.0
    p2_loss_average = 0.0

    for b in range(batches):
        seed = seed + b 
        (P1_observations_batch_tensor,
        P2_observations_batch_tensor,
        P1_positions_batch_tensor,
        P2_positions_batch_tensor,
        E1_positions_batch_tensor,
        mask_tensor,
        P1_positions_P2_batch_tensor) = batch(size, batch_size, t_max, seed)

        p1_loss, p2_loss = loss(p1_lstm, p2_lstm, P1_observations_batch_tensor, P2_observations_batch_tensor, P1_positions_batch_tensor, P2_positions_batch_tensor, E1_positions_batch_tensor, mask_tensor, P1_positions_P2_batch_tensor)
        p1_loss_average += p1_loss
        p2_loss_average += p2_loss 

    print(f"p1_lstm{hidden_state_size} loss average : {p1_loss_average / batches}")
    print(f"p2_lstm{hidden_state_size} loss average : {p2_loss_average / batches}")

if __name__ == "__main__":
    size = 15
    t_max = 50
    hidden_state_sizes = [256]
    batches = 50_000
    batch_size = 250
    learning_rate = 1e-3
    possible_positions = size*size 
    seed  = 199_999_999

    for hidden_state_size in hidden_state_sizes:
        random.seed(seed)
        np.random.seed(seed)
        torch.manual_seed(seed)

        p1_lstm = LSTM(hidden_state_size, possible_positions, device).to(device)
        p2_lstm = LSTM(hidden_state_size, possible_positions, device).to(device)

        p1_lstm_opt = torch.optim.Adam(p1_lstm.parameters(), lr=learning_rate)
        p2_lstm_opt = torch.optim.Adam(p2_lstm.parameters(), lr=learning_rate)

        for b in range(batches):
            seed = seed + b 
            (P1_observations_batch_tensor,
            P2_observations_batch_tensor,
            P1_positions_batch_tensor,
            P2_positions_batch_tensor,
            E1_positions_batch_tensor,
            mask_tensor,
            P1_positions_P2_batch_tensor) = batch(size, batch_size, t_max, seed)

            p1_loss, p2_loss = loss(p1_lstm, p2_lstm, P1_observations_batch_tensor, P2_observations_batch_tensor, P1_positions_batch_tensor, P2_positions_batch_tensor, E1_positions_batch_tensor, mask_tensor, P1_positions_P2_batch_tensor)
        
            p1_lstm_opt.zero_grad()
            p2_lstm_opt.zero_grad()

            p1_loss.backward()
            p2_loss.backward()

            torch.nn.utils.clip_grad_norm_(p1_lstm.parameters(), 5.0)
            torch.nn.utils.clip_grad_norm_(p2_lstm.parameters(), 5.0)

            p1_lstm_opt.step()
            p2_lstm_opt.step()

            if b % 250 == 0:
                print(f"Batch:{b}/{batches}, P1 loss was :{p1_loss}, P2 loss was: {p2_loss}")

        p1_lstm.stop()
        p2_lstm.stop()

        #validate(p1_lstm, p2_lstm, size, t_max, batch_size, hidden_state_size, batches = 2_500, seed = 999123999)

        torch.save(p1_lstm.state_dict(), f"PyTorch_Models/p1_lstm{hidden_state_size}.pt")
        torch.save(p2_lstm.state_dict(), f"PyTorch_Models/p2_lstm{hidden_state_size}.pt")







