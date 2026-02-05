#!/usr/bin/python3
"""
Module that defines the VerboseList class.
"""


class VerboseList(list):
    """
    A custom list class that prints notifications
    whenever items are added or removed.
    """

    def append(self, item):
        """
        Append item to the list and print a notification.
        """
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        """
        Extend the list with items from iterable and print a notification.
        """
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with {count} items.")

    def remove(self, item):
        """
        Remove item from the list and print a notification.
        """
        print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Pop item at index (default last) and print a notification.
        """
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)
