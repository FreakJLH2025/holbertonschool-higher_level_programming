#!/usr/bin/python3
"""
Module that defines the CountedIterator class.
"""


class CountedIterator:
    """
    A custom iterator that counts how many items
    have been iterated over.
    """

    def __init__(self, iterable):
        """
        Initialize with an iterable and set counter to 0.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """
        Return the iterator itself.
        """
        return self

    def __next__(self):
        """
        Return the next item and increment the counter.
        """
        item = next(self.iterator)  # may raise StopIteration
        self.count += 1
        return item

    def get_count(self):
        """
        Return the number of items that have been iterated.
        """
        return self.count
