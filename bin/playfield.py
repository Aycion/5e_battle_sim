"""
File: playfield.py -- Copyright Emery Bacon;   10/7/2018

"""
import random as rand
from bin.agent import *


class PlayingField:

    def __init__(self, pop_cap=5, bounds=(15, 15), grid_default=None):

        if pop_cap < 0:
            raise ValueError('Invalid population size: ', pop_cap)
        if bounds[0] < 1 or bounds[1] < 1:
            raise ValueError('Invalid coordinates: ', bounds)

        self.bounds = bounds
        (self._x_max, self._y_max) = bounds
        self._grid_default = grid_default

        self.agentPop = AgentPop(pop_cap)
        self._set_grid(self._grid_default)

    def get_bounds(self):
        return self.bounds

    def get_square(self, point):
        """
        Grab the contents of the grid point specified by state

        :param point: The gridpoint to check, tuple of (x, y) coords
        :return: Contents of the square corresponding to point; None if the square is empty
        """
        (x, y) = point
        if 0 <= x < self._x_max and 0 <= y < self._y_max:
            return self.grid[x][y]
        raise ValueError('Coordinates {} out of bounds.'.format((x, y)))

    def add_agent(self, agent, controller=None):
        if self.get_square(agent.get_state()):
            raise ValueError('Coordinates {} occupied'.format(agent.get_state()))

        self.grid[agent.get_x()][agent.get_y()] = agent
        agent.set_controller(controller)
        return self.agentPop.add(agent)

    def gen_rand_agents(self, count):
        """
        Generate a number of random agents specified by count

        :param count: The number of agents to create
        :return: The newly updated population of agents
        """

        while count > 0:
            rand_x = rand.randint(0, self._x_max - 1)
            rand_y = rand.randint(0, self._y_max - 1)
            agent = Agent(self, point=(rand_x, rand_y))

            try:
                self.add_agent(agent)
                count -= 1
            except ValueError as e:  # if square is occupied
                print(e)
                count -= 1
            except IndexError as e:  # if the population is full
                print(e)
                count = 0

        return self.agentPop

    def clear(self):
        self.agentPop = AgentPop(self.agentPop.limit)
        self._set_grid(self._grid_default)

    def print(self):
        for ag in self.agentPop:
            print(ag)

    def _set_grid(self, default=None):
        self.grid = [[default for _ in range(self._y_max)] for _ in range(self._x_max)]
