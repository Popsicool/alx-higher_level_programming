#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return (result)
    except BaseException as err:
        print("Exception: {0}".format(err), file=sys.stderr)
        return (None)
