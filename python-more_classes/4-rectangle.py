#!/usr/bin/python3
"""
This module defines a Rectangle class.

The class represents a geometric rectangle
with private attributes width and height.
It validates that width and height are
non-negative integers.
"""


class Rectangle:
    """
    This class defines a rectangle by its width and height.

    Both attributes are private and controlled through
    property getters and setters to ensure validation.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieve the width of the rectangle.

        Returns:
            int: The current width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle with validation.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieve the height of the rectangle.

        Returns:
            int: The current height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle with validation.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Compute the area of the rectangle.

        Returns:
            int: The current rectangle area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Compute the perimeter of the rectangle.

        Returns:
            int: The current rectangle perimeter.
                 If width or height is 0, perimeter is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return the string representation of the rectangle
        using the character '#'.

        If width or height is 0, return an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_lines = []
        for _ in range(self.__height):
            rect_lines.append("#" * self.__width)
        return "\n".join(rect_lines)

    def __repr__(self):
        """
        Return a string representation of the rectangle
        that can be used to recreate a new instance
        with eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"
