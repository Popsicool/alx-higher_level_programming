#!/usr/bin/python3
"""

Prints a square

"""


def print_square(size):
    """print square

    Args:
        size: size of square

    Raises:
        TypeError: If size is not an int 
        ValueError: If size is less than zero

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for n in range(0, size):
        for m in range(size):
            print("#", end="")
        print("")
