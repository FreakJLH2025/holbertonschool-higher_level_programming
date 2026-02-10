#!/usr/bin/python3
"""
Function that writes a string to a text file (UTF8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes text to a UTF8 file and returns
    the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
