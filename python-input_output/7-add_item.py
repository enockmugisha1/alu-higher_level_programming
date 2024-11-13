#!/usr/bin/python3

"""this is python."""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

def main():
    """Main function to add command-line arguments to a JSON file."""
    filename = 'add_item.json'
    
    # Load existing items from the JSON file, or initialize an empty list if it doesn't exist
    try:
        items = load_from_json_file(filename)
    except FileNotFoundError:
        items = []

    # Add command-line arguments to the list (excluding the script name)
    items.extend(sys.argv[1:])

    # Save the updated list back to the JSON file
    save_to_json_file(items, filename)

if __name__ == "__main__":
    main()
