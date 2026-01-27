#!/usr/bin/python3
"""
This module defines a Square class.
The class represents a geometric square with a private size attribute.
It validates that size is a non-negative integer, can compute its area,
and can print the square using the character '#'.
"""


class Square:
    """
    This class defines a square by its size.
    The size attribute is private to ensure control
    over its type and value. Getter and setter methods
    are provided to retrieve and update the size safely.
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
        self.size = size  # uses the setter for validation

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Compute the area of the square.

        Returns:
            int: The current square area.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square using the character '#'.

        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
