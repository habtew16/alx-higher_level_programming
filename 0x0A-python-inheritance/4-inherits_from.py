#!/usr/bin/python3
"""function that checks only inherits from"""


def inherits_from(obj, a_class):
    """Check if obj is an instance of a
    class that inherits from the specified class
    """
    if not isinstance(obj, type):
        return False
    return issubclass(obj, a_class)
