"""
File: controller.py -- Copyright Emery Bacon;   10/7/2018

Class file for the controller object.
Links to an agent or any compatible subclass, and
makes decisions for that agent.
"""

class Controller:

    def __init__(self, neighbors):
        self.neighbors = neighbors