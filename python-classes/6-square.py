#!/usr/bin/python3
"""
This module defines a Square class with size and position attributes.
The class includes methods to calculate area and print the square.
"""


class Square:
    """
    A class that represents a square with size and position attributes.
    
    Attributes:
        size (int): The length of the square's side
        position (tuple): The (x, y) position for printing
        
    Methods:
        area(): Returns the area of the square
        my_print(): Prints the square using '#' characters
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.
        
        Args:
            size (int): The size of the square, defaults to 0
            position (tuple): The position for printing, defaults to (0, 0)
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.
        
        Args:
            value (int): The new size value
            
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square with validation.
        
        Args:
            value (tuple): The new position value
            
        Raises:
            TypeError: If value is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.
        
        Returns:
            int: The area of the square (size * size)
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square using '#' characters considering position.
        
        If size is 0, prints an empty line.
        Position[0] adds spaces before each line (horizontal offset).
        Position[1] adds empty lines before the square (vertical offset).
        """
        if self.__size == 0:
            print()
            return

        # Print vertical offset (empty lines)
        for _ in range(self.__position[1]):
            print()

        # Print the square with horizontal offset
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
