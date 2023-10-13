#!/usr/bin/python3
"""function that checks only inherits from"""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a
    class that inherits from the specified class
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
