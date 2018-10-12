"""
File: driver.py -- Copyright Emery Bacon;   10/7/2018

"""
from display.g_window import *
from bin.controller import Controller


def __main__():

    field = playfield.PlayingField(pop_cap=100, bounds=(50, 40))
    gwin = GDriver(field=field, title='Graphical Example', grid_scale=15, border=10)
    gwin.field.gen_rand_agents(100)

    kb_control = Controller()
    gwin.field.agentPop.agents[0].set_controller(kb_control)

    gwin.draw()
    while not gwin.checkMouse():
        gwin.draw()


if __name__ == '__main__':
    __main__()
