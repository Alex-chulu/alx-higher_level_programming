#!/usr/bin/python3
""" function that inserts a line of text to a file, after each line containing
    a specific string
    """


def append_after(filename="", search_string="", new_string=""):
    """inserts/adds a line of text to a file

    Args:
        filename(str): File name.
        search_string(str): Searches for a specific string.
        new_string(str): Added text.
    """
    empt = ""
    with open(filename, encoding="UTF8") as file:
        for ls_line in file:
            if search_string in ls_line:
                empt += ls_line[:] + new_string
            else:
                empt += ls_line[:]
    with open(filename, mode="w", encoding="UTF8") as file:
        file.write(empt)
