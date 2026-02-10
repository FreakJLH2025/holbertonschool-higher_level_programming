#!/usr/bin/python3
"""
Script that adds all command-line arguments to a Python list
and saves them to a JSON file.
"""

import sys
import os

# Import the required functions
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def main():
    """
    Main function to handle adding arguments to list and saving to file
    """
    # Define the filename
    filename = "add_item.json"
    
    # Try to load existing data from the file
    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        # If file doesn't exist, start with an empty list
        my_list = []
    
    # Add all command-line arguments to the list
    # sys.argv[0] is the script name, so we skip it
    for arg in sys.argv[1:]:
        my_list.append(arg)
    
    # Save the updated list to the file
    save_to_json_file(my_list, filename)

if __name__ == "__main__":
    main()
