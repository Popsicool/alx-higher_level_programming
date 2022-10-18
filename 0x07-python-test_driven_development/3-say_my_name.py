#!/usr/bin/python3
""""
Module that print a name

"""


def say_my_name(first_name, last_name=""):
    '''Prints first nama and last name

    Args:
        first_name: first name
        last_name: last name

    Raises:
        TypeError: If names are not string

    '''

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
