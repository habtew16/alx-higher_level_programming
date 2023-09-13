#!/usr/bin/python3
def uniq_add(my_list=[]):
    sam = 0
    for i in set(my_list):
        sam += i
    return sam
