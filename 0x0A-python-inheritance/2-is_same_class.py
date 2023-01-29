#!/usr/bin/python3
""" The function will return True if the object is exactly an instance
    of the specified class; otherwise False.
    """


def is_same_class(obj, a_class):
    """
    Args:
        obj: object of different clases
        a_class: Class

    Returns:
        True: True if the object is exactly an instance
        of the specified class; otherwise False
    """
    return type(obj) is a_class
