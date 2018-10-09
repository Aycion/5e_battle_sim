"""
File: agent.py -- Copyright Emery Bacon;   10/7/2018

"""


class AgentPop:

    def __init__(self, limit = 5):
        self.agents = list()
        self.limit = limit
        self.size = 0

    def __iter__(self):
        return self.agents.__iter__()

    def add(self, agent):
        if self.size >= self.limit:
            raise IndexError('Population cap reached')
        self.agents.append(agent)
        self.update_all()

        self.size += 1
        return True

    def update_all(self):
        for ag in self.agents:
            ag.update_nb()
        return self



class Agent:

    def __init__(self, playing_field, controller=None, point=(-1, -1)):
        self.controller = controller
        self.playing_field = playing_field
        (self._x, self._y) = point
        self._set_neighbors()

    def get_state(self):
        return (self._x, self._y)

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_neighbors(self):
        return self.neighbors

    def move(self, dest):
        if self.state == dest:
            return False
        for nb in self.neighbors:
            if nb.state == dest:
                return False
        self.state = dest
        self._set_neighbors()


        return True

    def update_nb(self):
        self._set_neighbors()
        return self

    def _set_neighbors(self):
        (max_x, max_y) = self.playing_field.bounds
        (x, y) = self.get_state()
        self.neighbors = list()

        for nx in range(max(0, x - 1), min(x + 2, max_x)):
            for ny in range(max(0, y - 1), min(y + 2, max_y)):
                if not(nx == self._x and ny == self._y):
                    nb = self.playing_field.get_square((nx, ny))
                    if nb is not None:
                        self.neighbors.append(nb)
        return self.neighbors

    def __str__(self):
        toString = str(self.get_state()) + ':\n    Neighbors -- '
        if self.neighbors:
            for nb in self.neighbors:
                toString += str(nb.get_state())
        else:
            toString += str(None) + '\n'
        return toString