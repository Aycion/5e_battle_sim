"""
File: g_window.py -- Copyright Emery Bacon;   10/8/2018

"""

from bin import playfield, agent
from graphics import *

class GDriver(GraphWin):

    def __init__(self,
            field:playfield=None,
            title='Graphics Window',
            width:int=20, height:int=20,
            grid_scale=10,
            border=10):

        if field is not None:
            self.field = field
            (self.width, self.height) = field.get_bounds()
        else:
            self.field = self._gen_field(width, height)
            self.width = width
            self.height = height

        self.title = title
        self.grid_scale = grid_scale
        self.border = border

        super(GDriver, self).__init__(
            title=self.title,
            width=(self.width * self.grid_scale) + self.border/2,
            height=(self.height * self.grid_scale) + self.border/2)


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

    def draw(self):

        edge = self.border/2
        tl = Point(edge, edge)
        tr = Point(self.width - edge, edge)
        bl = Point(edge, self.height - edge)
        br = Point(self.width - edge, self.height - edge)

        line = Line(tl, tr)
        line.draw(self)
        line = Line(tr,br)
        line.draw(self)
        line = Line(br, bl)
        line.draw(self)
        line = Line(bl, tl)
        line.draw(self)

        for ag in self.field.agentPop:
            (x, y) = ag.get_state()
            ag_pt = Point((x * self.grid_scale) + 15, (y * self.grid_scale) + 15)
            if len(ag.get_neighbors()) > 0:
                ag_pt.setFill('red')
            ag_pt.draw(self)
