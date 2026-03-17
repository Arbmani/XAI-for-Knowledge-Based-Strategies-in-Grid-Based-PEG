import torch 
import torch.nn as nn 

class DQN(nn.Module):
    def __init__(self, hidden_state_size, possible_positions, device):
        super().__init__()

        self.device = device

        self.evader_to_hidden = nn.Sequential(
            nn.Linear(possible_positions, hidden_state_size),
            nn.ReLU(),
            nn.Linear(hidden_state_size, hidden_state_size // 2),
            nn.ReLU(),
        )

        self.teammate_to_hidden = nn.Sequential(
            nn.Linear(possible_positions, hidden_state_size),
            nn.ReLU(),
            nn.Linear(hidden_state_size, hidden_state_size // 2),
            nn.ReLU(),
        )

        self.q_values = nn.Sequential(
            nn.Linear(hidden_state_size + 2, (hidden_state_size + 2) // 2),
            nn.ReLU(),
            nn.Linear((hidden_state_size + 2) // 2, 4),
        )

    def forward(self, evader_probabilities, teammate_probabilities, agent_position):
        if not torch.is_tensor(agent_position):
            agent_position      = torch.tensor(agent_position, dtype=torch.float32, device=self.device).unsqueeze(0)

        evader_probabilities    = evader_probabilities.detach()
        teammate_probabilities  = teammate_probabilities.detach()


        evader_hidden           = self.evader_to_hidden(evader_probabilities)
        teammate_hidden         = self.teammate_to_hidden(teammate_probabilities)

        return self.q_values(torch.cat([evader_hidden, teammate_hidden, agent_position], dim=1))

