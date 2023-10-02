#!/usr/bin/python3

"Rectangle class"


class Rectangle:
    """
    this is rectangle class that does nothing
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    """
    width private data setter
    """
    @property
    def width(self):
        return self.__width

    """
    width data getter
    """
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    """
    height getter
    """
    @property
    def height(self):
        return self.__height

    """
    height setter
    """
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    """
    area calculator mathod
    """
    def area(self):
        return self.width * self.height

    """
    perimeter calculator
    """
    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.width + self. height)

    """
    method to modify __str__ object
    """
    def __str__(self):
        if not self.perimeter():
            return ""
        return ('\n'.join("{}".format(
            self.print_symbol) * self.width for x in range(self.height)))

    """
    eval method that recreates new instance
    """
    def __repr__(self):
        return ("Rectangle({}, {})".format(self.width, self.height))

    """
    delete rectangle
    """
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("{}".format("Bye rectangle..."))

    """
    finnd bigger recct from two'
    """
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
