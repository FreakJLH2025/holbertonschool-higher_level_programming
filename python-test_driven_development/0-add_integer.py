#!/usr/bin/python3
"""
This module provides a function to add two integers.

The function ensures that both arguments are integers or floats,
casts floats to integers, and raises a TypeError otherwise.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (casted to integers).

    Args:
        a: first number (int or float)
        b: second number (int or float, default 98)

    Returns:
        int: the sum of a and b

    Raises:
        TypeError: if a or b is not an integer or float, or is NaN/inf
    """
    # Validate a
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if isinstance(a, float):
        # NaN check: NaN != NaN; inf check: equals ±float('inf')
        if a != a or a == float('inf') or a == -float('inf'):
            raise TypeError("a must be an integer")

    # Validate b
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(b, float):
        if b != b or b == float('inf') or b == -float('inf'):
            raise TypeError("b must be an integer")

    return int(a) + int(b)
