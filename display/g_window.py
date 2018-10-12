"""
File: g_window.py -- Copyright Emery Bacon;   10/8/2018

"""

from bin import playfield
from graphics import *


def gen_field(width, height):
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


class GDriver(GraphWin):

    def __init__(
            self,
            field: playfield=None,
            title='Graphics Window',
            width: int=20,
            height: int=20,
            grid_scale=10,
            border=10):

        if field is not None:
            self.field = field
            (self.width, self.height) = field.get_bounds()
        else:
            self.field = gen_field(width, height)
            self.width = width
            self.height = height

        self.title = title
        self.grid_scale = grid_scale
        self.border = border
        self.win_width = (self.width * self.grid_scale) + self.border
        self.win_height = (self.height * self.grid_scale) + self.border

        super(GDriver, self).__init__(
            title=self.title,
            width=self.win_width,
            height=self.win_height)
        self.draw_grid()


    def draw_grid(self):  # Draw the grid
        for x in range(int(self.border / 2), self.win_width, self.grid_scale):
            p1 = Point(x, self.border/2)
            p2 = Point(x, self.win_height - (self.border/2))
            line = Line(p1, p2)
            line.draw(self)

        for y in range(int(self.border / 2), self.win_height, self.grid_scale):
            p1 = Point(self.border/2, y)
            p2 = Point(self.win_width - (self.border / 2), y)
            line = Line(p1, p2)
            line.draw(self)

    def read_kb(self):
        return self.checkKey()

    def draw(self):
        print('drawing')
        edge = self.border/2

        tl = Point(edge, edge)
        tr = Point(self.width - edge, edge)
        bl = Point(edge, self.height - edge)
        br = Point(self.width - edge, self.height - edge)


        line = Line(tl, tr)
        line.draw(self)
        line = Line(tr, br)
        line.draw(self)
        line = Line(br, bl)
        line.draw(self)
        line = Line(bl, tl)
        line.draw(self)


        self.field.agentPop.update_all()

        for ag in self.field.agentPop:
            if len(ag.get_neighbors()) > 0:
                color = 'red'
            elif ag.controller:
                color = 'blue'

            else:
                color = 'black'

            ag.draw(
                self,
                lambda pt: (pt * self.grid_scale) + edge + (self.grid_scale / 2),
                self.grid_scale,
                color
            )
