#!/usr/bin/python3
"""This is a function that adds a new attribute to an object"""


def add_attribute(object, name, value):
    """adds a new attribute to an object

    Args:
        obj(object): object of a class
        name(str): attribute description
        value(str): value contained

    Raises:
        TypeError: can't add new attribute.
        """
    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(object, name, value)
