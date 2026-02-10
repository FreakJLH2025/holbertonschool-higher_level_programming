#!/usr/bin/python3
"""
Class Student that defines a student by first_name, last_name, and age.
Provides JSON-style serialization and deserialization.
"""


class Student:
    """
    Student class with public attributes and methods
    to retrieve and reload dictionary representations.
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
        If attrs is a list of strings, only those attributes are included.
        Otherwise, all attributes are returned.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance
        using the provided dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
