3-say_my_name.py
#!/usr/bin/python3
"""Defines a function that prints a name."""


def say_my_name(first_name, last_name=""):
    """Print out name.

    Args:
        first_name (str): First name to be printed.
        last_name (str): Last name to be printed.

    Raise:
        TypeError: First_name or last_name must be a strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
