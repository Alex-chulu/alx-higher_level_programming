#!/usr/bin/python3
"""Defines a function to divide all elements of matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix (list): Lists of int or float.
        div (int/float): Divisor.

    Raise:
        TypeError: If the matrix contain non-numbers.
        TypeError: If the matrix contain rows of different sizes.
        TypeError: If divisor is not an int or float.
        ZeroDivisionError: If divisor is 0.

    Return:
        Nnew matrix representing the result of the division.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(elements, int) or isinstance(elements, float))
                    for elements in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
