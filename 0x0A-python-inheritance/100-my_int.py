#!/usr/bin/python3
"""This is a class MyInt that inherits from int"""


class MyInt(int):
    """MyInt class

    Args:
        int: superclass int
    """
    def __init__(self, i):
        """ class initialization

        Args:
            i(int): integer value
        """
        self.i = i

    def __equ__(self, some):
        """
        Returns:
            bool: boolean
        """
        return (self.i != some)

    def __ne__(self, some):
        """
        Args:
            some: description

        Returns:
            bool: boolean
        """
        return (self.i == some)
