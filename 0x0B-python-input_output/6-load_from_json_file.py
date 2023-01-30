#!/usr/bin/python3
"""This is a function that creates an Object from a JSON file"""


import json


def load_from_json_file(filename):
    """
    Args:
        filename: The name of a file
    """
    with open(filename, encoding="utf-8") as Json_File:
        return json.load(Json_File)
