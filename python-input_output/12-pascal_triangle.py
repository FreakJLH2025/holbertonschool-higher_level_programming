#!/usr/bin/python3
"""
Function that returns Pascal's triangle of n.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal's triangle of n.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # first row

    for i in range(1, n):
        prev_row = triangle[-1]
        # Start each row with 1
        row = [1]
        # Fill in the middle values
        for j in range(1, len(prev_row)):
            row.append(prev_row[j - 1] + prev_row[j])
        # End each row with 1
        row.append(1)
        triangle.append(row)

    return triangle
