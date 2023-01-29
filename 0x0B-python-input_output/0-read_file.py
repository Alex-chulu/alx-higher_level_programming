#!/usr/bin/python3
"""function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """
    Args:
        filename (str): The file name to open and read.
    """
    with open(filename, mode="r", encoding="UTF8") as MyFile:
        for line in MyFile:
            print(line, end="")
