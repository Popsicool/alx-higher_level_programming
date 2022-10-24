#!/usr/bin/python3
""" This module contains class MyInt that inherits from int"""


class MyInt(int):
    """class that inherits from int class"""

    def __eq__(self, value):
        """overide the default
        equals to operation"""

        return self.real != value

    def __ne__(self, value):
        """overide the default
        not equals to"""

        return self.real == value
