#!/usr/bin/python3
"""file handlin"""


def read_file(filename=""):
    """
    function to write on file
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read())
