#!/usr/bin/python3
import json
"""from json to object convertor"""


def from_json_string(my_str):
    """function to convert to obj"""
    return json.loads(my_str)
