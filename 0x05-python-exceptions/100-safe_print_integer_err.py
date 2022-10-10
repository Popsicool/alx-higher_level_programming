#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        state = True
        return (True)
    except BaseException as err:
        print("Exception: {0}".format(err), file=sys.stderr)
        return (False)
