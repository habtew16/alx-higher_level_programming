#!/usr/bin/python3
"""file handling"""
import json


def save_to_json_file(my_obj, filename):
    """function to save to json"""
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
