#!/usr/bin/python3
""" This module contains a class Rectangle
that inherits from BaseGeometry class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherites from class BaseGeometry"""

    def __init__(self, width, height):
        """initiates the class"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("width", height)
        self.__height = height

    def area(self):
        """return the area of the rectangle"""

        return (self.__width * self.__height)

    def __str__(self):
        """return the rectangle description"""

        string = "[" + str(self.__class__.__name__) + "]"
        string += str(self.__width) + "/" + str(self.__height)

        return string
