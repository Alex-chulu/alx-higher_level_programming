#!/usr/bin/python3

"""Defining a class Square."""

class Square:
    """This respresents a square."""

    def __init__(self, size=0):
        """Initializing new Square.

        Args:
            size (int): Size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise a ValueError("size must be >= 0")
        self.__size = size
