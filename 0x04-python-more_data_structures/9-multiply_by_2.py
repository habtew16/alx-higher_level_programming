#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a = {}
    for key, val in a_dictionary.items():
        a[key] = val * 2
    return a
