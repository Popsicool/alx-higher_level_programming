#!/usr/bin/python3
""" A class that defines a rectangle"""


class Rectangle:
    """ Rectangle class"""

    def __init__(self, width=0, height=0):
        """initialize the rectangle
        Args:
            width: Width of the rectangle
            height: Height of the rectangle
        raise:
            TypeError: if the passed value is not integer
            ValueError: if value passed is less than 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ makes the width property private"""

        return self.__width

    @width.setter
    def width(self, value):
        """Set the value for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """make the height prvate"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ calculate the area of the rectangle
        and return it"""

        return (self.__height * self.width)

    def perimeter(self):
        """return the perimeter of the rectangle
        or 0 if either width or height is 0"""

        if (self.__width == 0 or self.__height == 0):
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self) -> str:
        """ Return a string representation of the rectangle with #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for row in range(self.__height):
            for col in range(self.__width):
                rectangle += "#"
                if (col == (self.width - 1)):
                    rectangle += "\n"
        return (rectangle)
