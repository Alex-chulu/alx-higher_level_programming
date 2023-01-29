#!/usr/bin/python3
"""function that writes a string to a text file (UTF8) and returns
    the number of characters written
    """


def write_file(filename="", text=""):
    """
    Args:
        filename(str): The name of the file open and read.
        text(str): string to be written in the text file.

    Returns:
        number of characters written
    """
    with open(filename, mode="w", encoding="UTF8") as MyFile:
        return (MyFile.write(text))
