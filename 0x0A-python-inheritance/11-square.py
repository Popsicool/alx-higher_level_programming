#!/usr/bin/python3
""" This module contain
class Square that inherits from class Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Claa square that inherits from class rectangle"""

    def __init__(self, size):
        """initialize the square class"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
