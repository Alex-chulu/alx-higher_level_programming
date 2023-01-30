#!/usr/bin/python3
"""Max integer Unittests."""


def max_integer(list=[]):
    """Finds and returns max_integer in integer list."""
    if len(list) == 0:
        return None
    outcome = list[0]
    y = 1
    while y < len(list):
        if list[y] > outcome:
            outcome = list[y]
        y += 1
    return outcome
