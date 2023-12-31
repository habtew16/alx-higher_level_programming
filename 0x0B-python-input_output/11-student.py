#!/usr/bin/python3
"""conversion of json in clas"""


class Student:
    """init funciton"""
    def __init__(self, first_name, last_name, age):
        """initializer function to assign data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """function that converts self to json"""
        if(attrs and isinstance(attrs, list) and
           all(isinstance(x, str) for x in attrs)):
            return({x: y for x, y in self.__dict__.items() if x in attrs})
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replaces allattributes with json"""
        if(json):
            self.__dict__ = json
