import torch 
import torch.nn as nn

class LSTM(nn.Module):
    def __init__(self, hidden_state_size, possible_positions, device):
        super().__init__()
        
        self.device                 = device
        self.hidden_state_size      = hidden_state_size
        self.observation_size       = 8

        self.observation_to_hidden  = nn.Sequential(
            nn.Linear(self.observation_size, hidden_state_size),
            nn.ReLU(),
        )

        self.lstm                       = nn.LSTMCell(hidden_state_size, hidden_state_size)
        self.evader_belief_logit_map    = nn.Linear(hidden_state_size, possible_positions)
        self.teammate_belief_logit_map  = nn.Linear(hidden_state_size, possible_positions)

    def init_state(self, batch_size = 1):
        hidden_state    = torch.zeros(batch_size, self.hidden_state_size, device = self.device) 
        cell_state      = torch.zeros(batch_size, self.hidden_state_size, device = self.device) 
        return hidden_state, cell_state
        
    def forward(self, observation, hidden_state, cell_state):
        o_t = self.observation_to_hidden(observation)
            
        new_hidden_state, new_cell_state = self.lstm(o_t, (hidden_state, cell_state))
            
        evader_logits   = self.evader_belief_logit_map(new_hidden_state)
        teammate_logits = self.teammate_belief_logit_map(new_hidden_state)

        return new_hidden_state, new_cell_state, evader_logits, teammate_logits  
    
    def stop(self):
        self.requires_grad_(False)
        self.eval()


