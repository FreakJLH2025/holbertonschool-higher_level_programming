#!/usr/bin/python3
"""
Module that defines a CustomObject class with
serialization and deserialization using pickle.
"""

import pickle


class CustomObject:
    """
    CustomObject with attributes:
    - name (string)
    - age (integer)
    - is_student (boolean)
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Print the object's attributes in the required format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance and save it to the given filename.
        Returns None if serialization fails.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from the given filename.
        Returns an instance of CustomObject or None if deserialization fails.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except Exception:
            return None
