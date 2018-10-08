"""
File: agent.py -- Copyright Emery Bacon;   10/7/2018

"""


class AgentPop:

    def __init__(self, size):
        self.agents = list()
        self.limit = size

    def add(self, agent, field):
        if len(self.agents) > self.limit:
            return False
        if field.get_square(agent.state):
            return False

        try:
            self.agents.append(agent)
        except ValueError as e:
            print(e)
            return False

        self.limit += 1
        return True

class Agent:

    def __init__(self, controller, playing_field, point=(-1, -1), neighbors=None):
        self.controller = controller
        self.playing_field = playing_field
        self.state = point
        self.neighbors = neighbors if neighbors else []

    def move(self, dest):
        for nb in self.neighbors:
            if nb.state == dest or self.state == dest:
                return False
        self.state = dest


        return True

    def _set_neighbors(self):
        (max_x, max_y) = self.playing_field.bounds
        (x, y) = self.state
        self.neighbors = list()

        for nx in range(max(0, x - 1), min(x + 2, max_x + 1)):
            for ny in range(max(0, y - 1), min(y + 2, max_y + 1)):
                nb = self.playing_field.get_square(nx, ny)
                if nb is not None:
                    self.neighbors.append(nb)

        return self.neighbors
