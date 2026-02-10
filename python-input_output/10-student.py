#!/usr/bin/python3
"""
Class Student that defines a student by first_name, last_name, and age.
"""


class Student:
    """
    Student class with public attributes and a method
    to retrieve a dictionary representation.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of the Student instance.
        If attrs is a list of strings, only attributes contained in this list
        are retrieved. Otherwise, all attributes are returned.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__
