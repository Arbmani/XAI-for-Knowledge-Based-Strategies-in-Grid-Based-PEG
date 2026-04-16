from LSTM_train import validate
from action import device
from LSTM import LSTM 
import torch


if __name__ == "__main__":
    possible_positions = 15*15
    t_max = 50
    size = 15
    batch_size = 64
    batches = 200
    hidden_state_size = 256

    seed = 100000000000000000000000000000000000

    p1_knowledge_model = LSTM(hidden_state_size = 256, possible_positions = possible_positions, device=device).to(device)
    p1_knowledge_model.load_state_dict(torch.load(f"p1_lstm256.pt", map_location = device))
    p2_knowledge_model = LSTM(hidden_state_size = 256, possible_positions = possible_positions, device=device).to(device)
    p2_knowledge_model.load_state_dict(torch.load(f"p2_lstm256.pt", map_location = device))

    p1_knowledge_model.stop()
    p2_knowledge_model.stop()


    validate(p1_knowledge_model, p2_knowledge_model, size, t_max, batch_size, hidden_state_size, batches, seed)

