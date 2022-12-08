#!/usr/bin/python3
def number_keys(a_dictionary):
    number = 0
    list_of_keys = list(a_dictionary.keys())

    for x in list_of_keys:
        number += 1
    return (number)
