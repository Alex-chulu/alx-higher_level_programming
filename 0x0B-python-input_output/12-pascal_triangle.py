#!/usr/bin/python3
"""function that returns a list of lists of integers representing
    the Pascal’s triangle of n"""


def pascal_triangle(n):
    """Returns a list of integers

    Args:
        n(int): Integer

    Returns:
        a list of integers
    """
    if n <= 0:
        return []
    triangle = []

    for x in range(0, n):
        list_ls = []
        for y in range(0, x + 1):
            if y is 0 or y is x:
                list_ls.append(1)
            else:
                list_ls.append(triangle[x - 1][y - 1] + triangle[x - 1][y])
        triangle.append(list_ls)
    return 
