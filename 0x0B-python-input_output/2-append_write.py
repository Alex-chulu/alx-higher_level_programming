#!/usr/bin/python3
"""function that appends a string at the end of a text file
    (UTF8) and returns the number of characters added"""


def append_write(filename="", text=""):
    """add data to the end of the file.

    Args:
        filename(str): The name of the file open and apped data to
        text(str): string to add to the text in the file.

    Returns:
        number of characters added
    """
    with open(filename, mode="a", encoding="UTF8") as MyFile:
        return (MyFile.write(text))
