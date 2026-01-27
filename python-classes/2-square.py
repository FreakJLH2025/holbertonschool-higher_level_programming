#!/usr/bin/python3
"""
This module defines a Square class.
The class represents a geometric square with a private size attribute.
It validates that size is a non-negative integer.
"""


class Square:
    """
    This class defines a square by its size.
    The size attribute is private to ensure control
    over its type and value.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
