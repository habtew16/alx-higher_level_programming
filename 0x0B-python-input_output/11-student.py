#!/usr/bin/python3
"""file handling"""


class Student:
    """student class to retrieve JSON of self"""
    def __init__(self, first_name, last_name, age):
        """init function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves JSON of self"""
        if attrs is None:
            return self.__dict__

        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            return {x: y for x, y in self.__dict__.items() if x in attrs}
        else:
            return self.__dict__
