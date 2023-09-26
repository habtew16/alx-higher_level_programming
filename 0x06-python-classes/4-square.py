#!/usr/bin/python3
"square class"


class Square:
    """
    sqaure object
    """

    def __init__(self, size=0):
        self.__size = size
    """
    assign size to private property __size
    Args:
        __size(int): size of the square
    """
    @property
    def size(self):
        return self.__size
    """
    get the size of the square
    """
    @size.setter
    def size(self, value):
        if(type(value) is not int):
            raise TypeError("size must be an integer")
        if(value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
        """
        set the  size of  the square
        square must b > 0
        """
    def area(self):
        return(self.__size**2)
        """
        returns area
        """
