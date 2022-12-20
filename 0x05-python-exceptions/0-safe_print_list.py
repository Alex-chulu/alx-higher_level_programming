#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Args:
        my_list: list of elements.
        x: number of elements to print.
    Return: number of elements
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i], end=""))
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
