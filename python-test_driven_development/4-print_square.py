#!/usr/bin/python3
"""
Print a square of '#' characters with a given size.
"""


def print_square(size):
    """
    Prints a square with the character '#'.

    Args:
        size: the size length of the square (must be int)

    Raises:
        TypeError: if size is not an integer or is a float
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
