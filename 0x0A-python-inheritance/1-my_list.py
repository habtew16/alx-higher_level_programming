#!/usr/bin/python3
"""class that prints sorted list"""


class MyList(list):
    """function to print sorted list"""
    def print_sorted(self):
        print(sorted(self))
