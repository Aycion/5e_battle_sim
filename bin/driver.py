"""
File: driver.py -- Copyright Emery Bacon;   10/7/2018

"""
from display.g_window import *
import random as rand

def __main__():

    field = playfield.PlayingField(pop_cap=100, bounds=(50, 40))
    gwin = GDriver(field=field, title='Graphical Example', grid_scale=15, border=10)
    gwin.field.gen_rand_agents(90)
    # gwin.field.agentPop[0].move()
    # for ag in gwin.field.agentPop:
    #     rand.randint(1,11)
    #     if
    gwin.draw()
    gwin.getMouse()

# def random_move():


if __name__ == '__main__':
    __main__()
