"""
File: g_window.py -- Copyright Emery Bacon;   10/8/2018

"""

from bin import playfield, agent
from graphics import *

class GDriver(GraphWin):

    def __init__(self, title='Graphics Window', width:int=20, height:int=20, grid_scale=10, border=10):
        super(GDriver, self).__init__(title=title, width=(width * grid_scale) + border/2, height=(height * grid_scale) + border/2)
        self.grid_scale = grid_scale
        self.width = width
        self.heigh = height
        self.field = self._gen_field(width, height)
        # self.win = GraphWin()

    def _gen_field(self, width, height):
        """
        Generates a playing field of the specified width and height,
        and having a a population cap of 3/4 the available spaces

        :param width:
        :param height:
        :return: the generated PlayField object
        """
        return playfield.PlayingField(
            bounds=(width, height),
            pop_cap=width * height * .75  # limit pop to 3/4 the available space
        )

    def get_win(self):
        """Returns the window associated with the GDriver object"""
        return self.win