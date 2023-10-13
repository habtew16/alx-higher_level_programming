#!/usr/bin/python3
"""unction to return if obj is instance
o class"""


def is_same_class(obj, a_class):
    """function to check"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
