#!/usr/bin/python3
"""
This module provides a function to add two integers.
The function handles both integers and floats, converting floats to integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    
    Args:
        a: First number, must be integer or float
        b: Second number, must be integer or float, defaults to 98
    
    Returns:
        The sum of a and b as an integer
    
    Raises:
        TypeError: If a or b is not an integer or float
    
    Examples:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
        >>> add_integer(2)
        100
        >>> add_integer(2.5, 3.7)
        5
    """
    # Check if a is integer or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    
    # Check if b is integer or float  
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Cast to integers if they are floats
    a = int(a)
    b = int(b)
    
    # Return the sum
    return a + b
