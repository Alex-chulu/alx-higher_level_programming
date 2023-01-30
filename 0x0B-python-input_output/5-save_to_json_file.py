#!/usr/bin/python3
"""This is a function that writes an Object to a text file, using a JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """Writes and object to a tex file using JSON representation

    Args:
        my_obj: an object
        filename: The name of the file
        """
    with open(filename, mode="w", encoding="utf-8") as Json_File:
        Json_File.write(json.dumps(my_obj))
