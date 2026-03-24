import random 

Index_to_Action = [(-1, 0), (1, 0), (0, -1), (0, 1)]
Action_to_Index = {
    (-1, 0) : 0,
    ( 1, 0) : 1,
    (0, -1) : 2,
    (0,  1) : 3,
}

class Agent:
    def __init__(self, agent_id, position):
        self.id = agent_id
        self.position = position

class Game:
    def __init__(self, size, agents, pursuer_ids, evader_id, t_max):
        self.size = size
        self.agents = agents
        self.pursuer_ids = pursuer_ids
        self.evader_id = evader_id
        self.turn_order = [pursuer_ids[0], pursuer_ids[1], evader_id]
        self.t_max = t_max
        self.observed_actions_since_last_turn_array = {agent_id: [] for agent_id in agents.keys()}

    def new_position(self, position, action):
        x, y = position
        dx, dy = action 
        return (x + dx, y + dy)
    
    def valid_moves(self, position):
        moves = []
        for action in Index_to_Action:
            x, y = self.new_position(position, action)
            if 0 <= x < self.size and 0 <= y < self.size:
                moves.append(action)
        return moves
    
    def do_we_observe_agent(self, observer, agent):
        return observer[0] == agent[0] or observer[1] == agent[1]
    
    def is_evader_captured(self):
        evader_position = self.agents[self.evader_id].position
        for pursuer_id in self.pursuer_ids:
            if evader_position == self.agents[pursuer_id].position:
                return True
        return False

    def observe(self, observer_id, delete_observed_actions_since_last_turn_array = True):
        observer = self.agents[observer_id]

        visible_positions = {}
        for agent_id, agent in self.agents.items():
            if agent_id != observer_id and self.do_we_observe_agent(observer.position, agent.position):
                visible_positions[agent_id] = agent.position
        
        copy = self.observed_actions_since_last_turn_array[observer_id]
        if delete_observed_actions_since_last_turn_array:
            self.observed_actions_since_last_turn_array[observer_id] = []
        return visible_positions, copy
    
    def observed_actions_since_last_turn(self, agent_id, new_position, old_position):
        for observer_id, observer in self.agents.items():
            if agent_id != observer_id and (self.do_we_observe_agent(observer.position, old_position)
                                            or self.do_we_observe_agent(observer.position, new_position)):
                self.observed_actions_since_last_turn_array[observer_id].append((agent_id, old_position, new_position))
        
    def agent_move(self, agent_id, action):
        agent = self.agents[agent_id]
        old_position = agent.position
        agent.position = self.new_position(old_position, action)
        self.observed_actions_since_last_turn(agent_id, agent.position, old_position)

def Create_Game(size, t_max, seed):
    #random.seed(seed)

    def random_starting_position(size):
        positions = [(row, column) for row in range(size) for column in range(size)]
        random.shuffle(positions)
        return positions[:3]
    
    position_1, position_2, position_3 = random_starting_position(size)
    agents = {
        "P1": Agent("P1", position_1),
        "P2": Agent("P2", position_2),
        "E1": Agent("E1", position_3),
    }
    return Game(size, agents, ("P1", "P2"), "E1", t_max)

