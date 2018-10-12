"""
File: controller.py -- Copyright Emery Bacon;   10/7/2018

Class file for the controller object.
Links to an agent or any compatible subclass, and
makes decisions for that agent.
"""
from keyboard import *


class Controller:

    def __init__(self, agent=None, keymap: dict=None):
        self.nextdir = (0, 0)
        self.keymap = keymap if keymap else {
            'up': (0, -1),
            'down': (0, 1),
            'left': (-1, 0),
            'right': (1, 0)
        }
        self.agent = agent
        for key in self.keymap:
            on_press_key(key, callback=self.cmd_mv)

    def set_agent(self, agent):
        self.agent = agent

    def cmd_mv(self, x):
        self.agent.move(self.keymap[x.name])


