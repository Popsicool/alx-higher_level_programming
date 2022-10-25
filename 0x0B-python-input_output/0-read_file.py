#!/usr/bin/python3
""" This module contains
a function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """a function that reads a text file (UTF8) and prints it to stdout"""

    with open(filename, mode='r', encoding='utf-8') as file_name:
        print(file_name.read(), end="")
