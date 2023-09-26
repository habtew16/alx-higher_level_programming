#!/usr/bin/python3
"class square"


class Square:
    """
    class square with private instanec
    
    which has init function that
    is called immediatly in object creation
    """


    def __init__(self, size=0):
        if(type(size) is not int):
            raise TypeError("size must be an integer")
        if(size < 0):
            raise ValueError("size must be >= 0")

        self.__size = size
    """
    init is method which is called when
    class object is created and initiates
    private size
    args:
        __size(int): the size of the square
        size must be positive
    """
