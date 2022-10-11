#!/usr/bin/python3
"""define a class square"""


class Square:
    """Initialize square class"""
    def __init__(self, size=0):
        if (isinstance(size, int) is False):
            raise TypeError('size must be an integer')
        elif (size < 0):
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
    """Retrive size property"""
    @property
    def size(self):
        return self.__size
    """ Set size property"""
    @size.setter
    def size(self, value):
        if (isinstance(value, int) is False):
            raise TypeError('size must be an integer')
        elif (value < 0):
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
    """ Area method"""
    def area(self):
        return self.__size ** 2
    """ Print square"""
    def my_print(self):
        if self.__size == 0:
            print()
        return
        i = 0
        while (i < self.__size):
            j = 0
            while (j < self.__size):
                print("#", end="")
                j += 1
            print()
            i += 1
