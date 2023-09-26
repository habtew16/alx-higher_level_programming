#!/usr/bin/python3
"Defines a class Square"


class Square:
    """square class has method area to find area"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """
    method for area of the square
    Args:
    __size(int): size of the square
    """


    def area(self):
        return(self.__size ** 2)

    "return area of the sqaure"
