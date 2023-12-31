#!/usr/bin/python3
"""file handling"""
import json


def load_from_json_file(filename):
    """function to load from json"""
    with open(filename, mode='r', encoding="utf-8") as f:
        data = json.load(f)
    return data
