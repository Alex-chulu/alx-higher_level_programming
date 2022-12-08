#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ordered_keys = list(a_dictionary.keys())
    ordered_keys.sort()

    for x in ordered_keys:
        print("{}: {}".format(x, a_dictionary.get(x)))
