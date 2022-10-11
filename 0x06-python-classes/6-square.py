#!/usr/bin/python3
""" declare class Square"""


class Square:
    "Initialize square"""
    def __init__(self, size=0, position=(0, 0)):
        if (isinstance(size, int) is False):
            raise TypeError('size must be an integer')
        elif (size < 0):
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
        self.__position = position
    "Retrive position property"""
    @property
    def position(self):
        return self.__position
    """ Set Position"""
    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) and (value[0] > 0 and value[1] > 0)):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    """ retrive size property"""
    @property
    def size(self):
        return self.__size
    """Set sizeproperty"""
    @size.setter
    def size(self, value):
        if (isinstance(value, int) is False):
            raise TypeError('size must be an integer')
        elif (value < 0):
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
    """  Area method"""
    def area(self):
        return self.__size ** 2
    """ prnt method"""
    def my_print(self):
        if self.__size == 0:
            print()
            return
        a = 0
        while (a < self.position[1]):
            print()
            a += 1

        i = 0
        while (i < self.__size):
            j = 0
            k = 0
            while (k < self.position[0]):
                print("_", end="")
                k += 1
            while (j < self.__size):
                print("#", end="")
                j += 1
            print()
            i += 1
