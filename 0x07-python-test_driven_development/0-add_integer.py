#!/usr/bin/python3
"""

add two numbers

"""


def add_integer(a, b=98):
    """Return:
        the sum of two the two numbers

    Args:
        a: arg1
        b: sarg2
    Raises:
        TypeError: If either of the args is not an integer or a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
