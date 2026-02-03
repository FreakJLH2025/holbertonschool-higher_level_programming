#!/usr/bin/python3
"""
Module that defines the is_kind_of_class function.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or if obj is an
    instance of a subclass of a_class; otherwise returns False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance or subclass instance of a_class,
        False otherwise.
    """
    return isinstance(obj, a_class)
