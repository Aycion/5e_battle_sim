"""
File: driver.py -- Copyright Emery Bacon;   10/7/2018

"""
from display.g_window import *

def __main__():

    field = playfield.PlayingField(pop_cap=20, bounds=(50, 40))
    gwin = GDriver(field=field, title='Graphical Example', grid_scale=15, border=10)
    gwin.field.gen_rand_agents(20)
    gwin.draw()
    gwin.getMouse()


if __name__ == '__main__':
    __main__()