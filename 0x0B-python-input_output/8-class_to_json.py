#!/usr/bin/python3
"""This is a function that returns the dictionary description with simple data structure"""


def class_to_json(obj):
    """
    Args:
        obj: an instance of a class

    Returns:
        dictionary description with simple data structure
    """
    return obj.__dict__
