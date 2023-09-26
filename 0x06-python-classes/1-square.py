#!/usr/bin/python3
"class square"


class Square:
    """class square with private instanec"""
    def __init__(self, size):
        self.__size = size
    """
    init is method which is called when
    class object is created and initiates
    private size
    args:
        __size(int): the size of the square
    """
