#!/usr/bin/python3
"""base class for the almost circle"""


class Base:
    __nb_objects = 0
    """init function"""
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
