import numpy as np
from action import get_observation

# True Knowledge Based Update Function
class KBU:
    def __init__(self, size):
        self.size                           = size 
        self.possible_positions             = size * size 
        self.evader_possible_locations      = np.ones(self.possible_positions, dtype=np.float32)
        self.teammate_possible_locations    = np.ones(self.possible_positions, dtype=np.float32)

    def init_state(self):
        self.evader_possible_locations      = np.ones(self.possible_positions, dtype=np.float32)
        self.teammate_possible_locations    = np.ones(self.possible_positions, dtype=np.float32)
    
    def forward(self, agent_id, game):
        def get_pos(observation):
            observation         = observation.detach().cpu().numpy()
            evader_position     = None if int(observation[2]) == 0 else (int(observation[3]) * self.size + int(observation[4]))
            teammate_position   = None if int(observation[5]) == 0 else (int(observation[6]) * self.size + int(observation[7]))

            return evader_position, teammate_position
        
        evader_position, teammate_position  = get_pos(get_observation(agent_id, game, delete_observed_actions_since_last_turn_array=True))
        agent_row, agent_column             = game.agents[agent_id].position
        visible_positions                   = {agent_row * self.size + col for col in range(self.size)} | {row * self.size + agent_column for row in range(self.size)}

        def update_possible_locations(position, possible_locations):
            new_possible_locations = np.zeros(self.possible_positions, dtype=np.float32)

            if position is not None:
                new_possible_locations[position] = 1.0
                return new_possible_locations

            for location in np.flatnonzero(possible_locations == 1.0):
                row, column = divmod(location, self.size)
                valid       = game.valid_moves((row, column))
                for dx, dy in valid:
                    new_possible_locations[(row + dx) * self.size + (column + dy)] = 1.0

            new_possible_locations[np.fromiter(visible_positions, dtype=np.int32)] = 0.0
            return new_possible_locations

        self.evader_possible_locations      = update_possible_locations(evader_position, self.evader_possible_locations) 
        self.teammate_possible_locations    = update_possible_locations(teammate_position, self.teammate_possible_locations)

        return (self.evader_possible_locations / self.evader_possible_locations.sum()), (self.teammate_possible_locations / self.teammate_possible_locations.sum())


