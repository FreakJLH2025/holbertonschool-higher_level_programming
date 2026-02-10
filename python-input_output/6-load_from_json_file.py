#!/usr/bin/python3
"""
Function that creates an Object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Reads a JSON file and returns the corresponding Python object.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
