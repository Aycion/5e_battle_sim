"""
File: playfield.py -- Copyright Emery Bacon;   10/7/2018

"""
import random as rand
from bin.agent import *

class PlayingField:

    def __init__(self, agents=AgentPop(0), bounds=(15,15)):
        self.bounds = bounds
        self._x_max = bounds[0]
        self._y_max = bounds[1]
        self.agentPop = agents
        self.grid = [[x for x in range(self._x_max)] for _ in range(self._y_max + 1)]

    def get_square(self, point):
        """
        Grab the contents of the grid point specified by state

        :param point: The gridpoint to check, tuple of (x, y) coords
        :return: Contents of the square corresponding to point; None if the square is empty
        """
        (x, y) = point
        if 0 <= x <= self._x_max and 0 <= y <= self._y_max:
            return self.grid[x][y]
        raise ValueError('Value out of bounds')

    def _gen_rand_agents(self, count):
        """
        Generate a number of random agents specified by count

        :param count: The number of agents to create
        :return: The newly updated population of agents
        """
        for _ in range(count):
            rand_x = rand.randint(0, self._x_max)
            rand_y = rand.randint(0, self._y_max)
            agent = Agent(self,(rand_x, rand_y))
            self.agentPop.add(agent, self)
        return self.agentPop

    def add_agent(self, agent):

        self.agentPop.add(agent, self)

