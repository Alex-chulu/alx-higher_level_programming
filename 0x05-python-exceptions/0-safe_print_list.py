#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Args:
        my_list: list of elements.
        x: number of elements to print.
    Return: number of elements
    """
    rmp = 0
    for y in range(x):
        try:
            print("{}\n".format(my_list[y], end=""))
            rmp += 1
        except IndexError:
            break
    print("")
    return (rmp)
