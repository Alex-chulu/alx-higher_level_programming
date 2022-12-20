#!/usr/bin/python3

def safe_print_integer(value):
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
