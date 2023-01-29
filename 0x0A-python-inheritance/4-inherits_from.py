#!/usr/bin/python3
"""This function will return True if the object
    is an instance of a class that it inherited
    (directly or indirectly) from the specified
    class ; otherwise False.
   """


def inherits_from(obj, a_class):
    """
    Args:
        obj: object of a class
        a_class: A class

    Returns:
        True: True if the object is an instance of a class
        that inherited; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not 
