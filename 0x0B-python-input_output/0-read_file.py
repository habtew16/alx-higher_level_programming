#!/usr/bin/python3
"""file handlin"""


def read_file(filename=""):
    """
    function to write on file
    """
    with open(filename, mode='r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
