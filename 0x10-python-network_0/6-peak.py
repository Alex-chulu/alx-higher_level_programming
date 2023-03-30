#!/usr/bin/python3
"""function that will find a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """pike function"""
    if len(list_of_integers) == 0:
        return
    list_of_integers.sort()
    return list_of_integers[-1]
