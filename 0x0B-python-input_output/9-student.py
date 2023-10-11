#!/usr/bin/python3
"""file handling"""


class Student:
    """student class to retrieve json of self"""
    def __init__(Self, first_name, last_name, age):
        """init funciont"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves json of self"""
        return self.__dict__
