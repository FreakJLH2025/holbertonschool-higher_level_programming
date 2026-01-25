#!/usr/bin/python3
"""
Divide all elements of a matrix by a number, rounding to 2 decimals.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounding to 2 decimals.

    Args:
        matrix: list of lists of integers/floats
        div: number (int or float)

    Returns:
        list of lists: new matrix with divided values

    Raises:
        TypeError: invalid matrix or div
        ZeroDivisionError: if div is zero
    """
    msg_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    msg_rows = "Each row of the matrix must have the same size"
    msg_div = "div must be a number"

    if not isinstance(matrix, list):
        raise TypeError(msg_matrix)
    if any(not isinstance(row, list) for row in matrix):
        raise TypeError(msg_matrix)
    if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
        raise TypeError(msg_matrix)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError(msg_rows)
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(msg_matrix)

    if not isinstance(div, (int, float)):
        raise TypeError(msg_div)
    if isinstance(div, float):
        if div != div or div == float('inf') or div == -float('inf'):
            raise TypeError(msg_div)
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
