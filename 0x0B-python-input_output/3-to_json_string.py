#!/usr/bin/python3
"""json convertor"""
import json


def to_json_string(my_obj):
    """function to convert string to json"""
    jstring = json.dumps(my_obj)
    return jstring
