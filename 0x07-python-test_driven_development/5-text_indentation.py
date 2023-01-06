#!/usr/bin/python3
"""Defines a function that indent text."""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: '.'',' '?' and ':'.

    Args:
        text (string): Text to be printed.

    Raise:
        TypeError: text must be a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    x = 0
    while x < len(text) and text[x] == ' ':
        x += 1

    while x < len(text):
        print(text[x], end="")
        if text[x] == "\n" or text[x] in ".?:":
            if text[x] in ".?:":
                print("\n")
            x += 1
            while x < len(text) and text[x] == ' ':
                x += 1
            continue
        x += 1
