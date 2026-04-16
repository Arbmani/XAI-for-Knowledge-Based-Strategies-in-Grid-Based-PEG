import torch 
import torch.nn as nn

class LSTM_BOB(nn.Module):
    def __init__(self, first_hidden_state_size, hidden_state_size, possible_positions, device):
        super().__init__()
        
        self.device                 = device
        self.hidden_state_size      = hidden_state_size
        
        self.observation_to_hidden          = nn.Sequential(
            nn.Linear(8 + 3 + 1, 32),
            nn.ReLU(),
        )

        self.beliefs_to_hidden              = nn.Sequential(
            nn.Linear(possible_positions * 2, hidden_state_size),
            nn.ReLU(),
        )

        self.first_order_states_to_hidden    = nn.Sequential(
            nn.Linear(first_hidden_state_size * 2, hidden_state_size),
            nn.ReLU(),
        )

        self.Three_2_1                          = nn.Sequential(
            nn.Linear(32 + 2*hidden_state_size, hidden_state_size),
            nn.ReLU(),
        )

        self.gate                               = nn.Sequential(
            nn.Linear(32 + 3 * hidden_state_size, hidden_state_size),
            nn.Sigmoid()
        )


        self.lstm                                = nn.LSTMCell(hidden_state_size, hidden_state_size)
        self.teammate_evader_belief_logit_map    = nn.Linear(hidden_state_size, possible_positions)
        self.teammate_teammate_belief_logit_map  = nn.Linear(hidden_state_size, possible_positions)

    def init_state(self, batch_size = 1):
        hidden_state    = torch.zeros(batch_size, self.hidden_state_size, device = self.device) 
        cell_state      = torch.zeros(batch_size, self.hidden_state_size, device = self.device) 
        return hidden_state, cell_state
        
    def forward(self, observation, observed_teammate_actions, evader_belief_logit_map, teammate_belief_logit_map, first_hidden_state, first_cell_state, hidden_state, cell_state, time_left):
        if not torch.is_tensor(time_left):
            time_left      = torch.tensor(time_left, dtype=torch.float32, device=self.device)
        time_left = time_left.unsqueeze(1)
        
        old_states      = self.first_order_states_to_hidden(torch.cat([first_hidden_state, first_cell_state], dim = 1))

        agent_beliefs   = self.beliefs_to_hidden(torch.cat([evader_belief_logit_map, teammate_belief_logit_map], dim=1))

        o_t             = self.observation_to_hidden(torch.cat([observation, observed_teammate_actions, time_left], dim=1))

        concat          = self.Three_2_1(torch.cat([o_t, agent_beliefs, old_states], dim=1))

        gate            = self.gate(torch.cat([o_t, agent_beliefs, old_states, hidden_state], dim=1))

        lstm_input      = old_states + gate * (concat - old_states) 

        new_hidden_state, new_cell_state = self.lstm(lstm_input, (hidden_state, cell_state))
            
        teammate_evader_logit   = self.teammate_evader_belief_logit_map(new_hidden_state)
        teammate_teammate_logit = self.teammate_teammate_belief_logit_map(new_hidden_state)

        return new_hidden_state, new_cell_state, teammate_evader_logit, teammate_teammate_logit  
    
    def stop(self):
        self.requires_grad_(False)
        self.eval()