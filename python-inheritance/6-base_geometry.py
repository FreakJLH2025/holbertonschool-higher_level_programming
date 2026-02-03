#!/usr/bin/python3
"""
Module that defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    BaseGeometry class with a public instance method area.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
