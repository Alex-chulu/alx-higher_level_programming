#!/usr/bin/python3
"""This function will return True if the object is an instance of,
   or if the object is an instance of a class that it inherited from,
   the specified class ; otherwise False.
   """


def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: object of a class
        a_class: A classes

    Returns:
        True: True if the object is an instance, or if the object is an instance
        of a class that it inherited from; otherwise False
    """
    return isinstance(obj, a_class)
