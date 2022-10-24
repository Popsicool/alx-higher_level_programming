#!/usr/bin/python3

""" This module contains the class BaseGeometry"""


class BaseGeometry:
    """ A non empty class"""

    def area(self):
        """ A non implemented method"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method that validate value"""

        if (type(value) != int):
            raise TypeError("{} must be an integer".format(value))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
