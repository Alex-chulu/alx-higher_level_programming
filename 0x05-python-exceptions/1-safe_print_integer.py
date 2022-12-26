#!/usr/bin/python3
def safe_print_integer(value):
<<<<<<< HEAD
"""
Args:
value: int to be printed
Return: True if no error occured else Fals
"""
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError)
    return (False)
=======
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
>>>>>>> c4f34168469fe518549cfdd56cec8829a1f70414
