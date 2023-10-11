#!/usr/bin/python3
"""from json to object convertor"""
import json


def from_json_string(my_str):
    """function to convert to obj"""
    return json.loads(my_str)
