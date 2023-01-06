#!/usr/bin/python3
""" Defining function that adds two integers. """


def add_integer(a, b=98):
    """ Returning the addition of two integers, a and b.
    a and b must be integers or floats.
    a and b must be first casted to integers if they are float.

    Raise:
        TypeError: a must be an integer or b must be an integer.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
