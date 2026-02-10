#!/usr/bin/python3
"""
Script that adds all arguments to a Python list
and saves them to a file in JSON format.
"""

import sys
from pathlib import Path
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

if Path(filename).exists():
    items = load_from_json_file(filename)
else:
    items = []

items.extend(sys.argv[1:])
save_to_json_file(items, filename)
