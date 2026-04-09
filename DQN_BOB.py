import torch 
import torch.nn as nn 


class DQN_BOB(nn.Module):
    def __init__(self, hidden_state_size, possible_positions, device):
        super().__init__()
        self.device = device
        self.possible_positions = possible_positions
        self.size               = int(possible_positions**0.5)
        self.cnn = nn.Sequential(
            nn.Conv2d(5, 16, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(16, 32, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(32, 32, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
        )

        self.mlp = nn.Sequential(
            nn.Linear(512 + 1, 128),
            nn.ReLU(),
            nn.Linear(128, 4),
        )



    def forward(self, evader_probabilities, teammate_probabilities, teammate_evader_probabilities, teammate_teammate_probabilities, agent_position, time_left):
        if not torch.is_tensor(agent_position):
            agent_position      = torch.tensor(agent_position, dtype=torch.float32, device=self.device)
        if not torch.is_tensor(time_left):
            time_left      = torch.tensor(time_left, dtype=torch.float32, device=self.device)
        time_left = time_left.unsqueeze(1)

        batch_size = evader_probabilities.shape[0]

        evader_map      = evader_probabilities.view(batch_size, 1, self.size, self.size)
        teammate_map    = teammate_probabilities.view(batch_size, 1, self.size, self.size)

        teammate_evader_map      = teammate_evader_probabilities.view(batch_size, 1, self.size, self.size)
        teammate_teammate_map    = teammate_teammate_probabilities.view(batch_size, 1, self.size, self.size)

        agent_map       = torch.zeros(batch_size, self.size, self.size, device = self.device)
        agent_map[torch.arange(batch_size, device=self.device), agent_position[:,0].long(), agent_position[:,1].long()] = 1.0
        agent_map = agent_map.unsqueeze(1)

        cnn_output      = self.cnn(torch.cat([evader_map, teammate_map, teammate_evader_map, teammate_teammate_map, agent_map], dim=1)).view(batch_size, -1)
        return self.mlp(torch.cat([cnn_output, time_left], dim=1))


    def stop(self):
        self.requires_grad_(False)
        self.eval()