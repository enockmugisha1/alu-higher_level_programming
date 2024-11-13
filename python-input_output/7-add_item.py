#!/usr/bin/python3
"""
Module 7-add_item
A script that adds all command-line arguments to a list and saves it to a JSON file.
"""

import sys
import os
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

filename = "add_item.json"

# Load existing data from the file if it exists, otherwise start with an empty list
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add new command-line arguments to the list
items.extend(sys.argv[1:])

# Save the updated list back to the JSON file
save_to_json_file(items, filename)
