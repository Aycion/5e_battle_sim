"""
File: agent.py -- Copyright Emery Bacon;   10/7/2018

"""
import operator
from bin.controller import Controller
from graphics import GraphWin, Point, Circle

class AgentPop:

    def __init__(self, limit = 5):
        self.agents = list()
        self.controlled = list()
        self.limit = limit
        self.size = 0

    def __iter__(self):
        return self.agents.__iter__()

    def add(self, agent):
        if self.size >= self.limit:
            raise IndexError('Population cap reached')
        self.agents.append(agent)
        if agent.controller:
            self.controlled.append(agent)
        self.update_all()

        self.size += 1
        return True

    def move(self, agent, dest):
        """
        Move the specified
        :param agent:
        :param dest:
        :return:
        """
        if agent not in self.agents:
            raise ValueError('Specified agent not in population')
        try:
            if type(agent) is Agent:
                agent.move(dest)
            elif type(agent) is list():
                return self._move_all(agent, dest)
        finally:
            self.update_all(force=True)

    def _move_all(self, agents, delta):
        """
        Function to call move on all the agents in the
        population. Used when the move method is called
        and passed a list of agents rather than just one
        :param agents:
        :param delta:
        :return:
        """
        for ag in agents:
            ag.move(delta)

    def update_all(self, force=False):
        """
        Calls each agent's 'update' function.
        Used when adding, moving, and removing agents
        with respect to the playing field
        """
        for ag in self.agents:
            if ag.moved or force:
                ag.update()


class Agent:

    def __init__(self,
                 playing_field,
                 point=(-1, -1),
                 controller=None):
        self.playing_field = playing_field
        self.state = point
        (self._x, self._y) = point
        self.update_neighbors()
        self.controller = controller
        self.set_controller(controller)
        self.moved = False

############################## Interface Functions ##############################
    def get_state(self):
        return (self._x, self._y)

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_neighbors(self):
        return self.neighbors

    def get_controller(self):
        return self.controller

    def set_controller(self, controller: Controller=None):
        if controller:
            self.controller = controller
            self.controller.set_agent(self)

    ############################# Worker Functions #############################

    def move(self, delta: tuple):
        # Element-wise tuple addition -- adds the delta tuple to the
        # state tuple, giving a new destination

        newstate = tuple(map(operator.add, self.state, delta))
        try:
            if self.playing_field.get_square(newstate):
                return False
        except ValueError as e:
            print(e)
            return False
        print('move called, moved to ', newstate)
        self.state = newstate
        (self._x, self._y) = self.state
        self.moved = True

        return True

    def update(self):
        self.update_neighbors()
        self.moved = False

        for nb in self.neighbors:
            nb.update_neighbors()
        return self

    ############################ Graphical Functions ############################

    def draw(self, win: GraphWin, offset_func, scale, color):
        (x, y) = self.state
        pt = Point(offset_func(x), offset_func(y))
        circ = Circle(pt, scale/2)
        circ.setFill(color)
        circ.draw(win)

    ############################# Private functions #############################
    def update_neighbors(self):
        (max_x, max_y) = self.playing_field.bounds
        (x, y) = self.get_state()
        self.neighbors = list()
        print('updating list')

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