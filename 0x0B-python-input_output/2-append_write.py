#!/usr/bin/python3
"""file handling"""


def append_write(filename="", text=""):
    """funnction to append on file"""
    with open(filename, mode='a', encoding="utf-8") as f:
        num_chars = f.write(text)
    return num_chars
