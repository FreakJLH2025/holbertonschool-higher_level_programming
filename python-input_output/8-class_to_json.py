#!/usr/bin/python3
"""
Function that returns the dictionary description
with simple data structure for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of obj
    with serializable attributes.
    """
    return obj.__dict__
