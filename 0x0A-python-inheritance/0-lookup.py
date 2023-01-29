#!/usr/bin/python3
"""returns the list ofavailable attributes
    and methods of an object
    """


def lookup(obj):
    """
    The dir() function will return a list of available attributes and
    methods of an object.

    Args:
        obj (list): object of the class object

    Returns:
        list: list of object
    """
    return dir(obj)

