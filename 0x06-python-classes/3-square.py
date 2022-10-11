#!/usr/bin/python3
""" Declare class square"""


class Square:
    """Initialize class square"""
    def __init__(self, size=0):
        if (isinstance(size, int) is False):
            raise TypeError('size must be an integer')
        elif (size < 0):
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
    """ Declare area method"""
    def area(self):
        return self.__size ** 2
