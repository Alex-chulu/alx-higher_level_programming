#!/usr/bin/python3
"""This is a function that returns the JSON representation of an object (string)"""


import json


def to_json_string(my_obj):
    """dumps: JSON Encoding

    Args:
        my_obj: object to be encoded

    Returns:
        JSON(string): JSON representation of an 0bject
    """
    return (json.dumps(my_obj))
