#!/usr/bin/python3
"""
Module that defines an abstract Shape class,
and concrete classes Circle and Rectangle.
Also defines a function shape_info that uses duck typing.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class Shape.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to compute the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to compute the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Circle class that inherits from Shape.
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class that inherits from Shape.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of any shape-like object.
    Relies on duck typing: assumes the object has area() and perimeter().
    """
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())


# Testing
if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    print("Circle info:")
    shape_info(circle)

    print("\nRectangle info:")
    shape_info(rectangle)
