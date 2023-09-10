#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        larg = my_list[0]
        for number in my_list:
            if number >= larg:
                larg = number
        return larg
