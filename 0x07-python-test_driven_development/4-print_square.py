#!/usr/bin/python3
"""Defines a function that prints a square."""


def print_square(size):
    """prints a square with the character #.

    Args:
        size (int): The size length of the square.

    Raise:
        TypeError: Size must be an integer.
        ValueError: Size must be  >= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for y in range(size):
        [print("#", end="") for x in range(size)]
        print("")
