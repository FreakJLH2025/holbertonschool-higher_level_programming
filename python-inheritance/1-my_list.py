#!/usr/bin/python3
"""
Module that defines the MyList class.
"""


class MyList(list):
    """
    MyList class that inherits from list and
    provides an additional method to print the list sorted.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        Assumes all elements are integers.
        """
        print(sorted(self))
