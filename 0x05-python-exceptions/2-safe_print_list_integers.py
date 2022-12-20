#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    Args:
        my_list: element list
        x: number of elements to access in my_list
    Return: number of integers printed

    rmp = 0
    for y in range(0, x):
        try:
            print("{:d}\n".format(my_list[y]), end="")
            rmp += 1
        except (TypeError, ValueError):
            continue
    return (rmp)
