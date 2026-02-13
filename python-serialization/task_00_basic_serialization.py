#!/usr/bin/python3
"""
Basic serialization module:
- serialize_and_save_to_file: saves a Python dictionary to a JSON file
- load_and_deserialize: loads a JSON file and returns a Python dictionary
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.
    If the file already exists, it will be replaced.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load a JSON file and deserialize it back into a Python dictionary.
    Returns the dictionary with the data.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
