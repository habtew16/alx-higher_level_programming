#!/usr/bin/python3
"""file handling"""


def write_file(filename="", text=""):
    """funnction to write on file"""
    with open(filename, mode='w', encoding="utf-8") as f:
        return(f.write(text))
