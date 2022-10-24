#!/usr/bin/python3
""" This module contains a function that returns True
if the object is an instance of a class that inherited
(directly or indirectly) from the specified class ;
otherwise False"""


def inherits_from(obj, a_class):
    """Check if obj is an instaance of the class that inherited
    from a specified class"""

    return (issubclass(type(obj), a_class) and type(obj) != a_class)
