#!/usr/bin/python3
""" Declare class square"""


class Square:
    """initialize class"""
    def __init__(self, size=0):
        self.__size = size
        """set size method"""
    @property
    def size(self):
        return self.__size
    """ define setter for size"""
    @size.setter
    def size(self, value):
        if (isinstance(value, int) is False):
            raise TypeError('size must be an integer')
        elif (value < 0):
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
    """ area method"""
    def area(self):
        return self.__size ** 2

    def __le__(self, other):
        return self.area() <= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()
