#!/usr/bin/python3
import sys
import json
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_to_list_and_save(args):
    """
    Add all arguments to a Python list and save them to a JSON file.
    
    Args:
        args: List of arguments to be added to the list.
    """
    try:
        data = load_from_json_file("add_item.json")
    except:
        data = []
    
    data.extend(args)
    
    save_to_json_file(data, "add_item.json")

if __name__ == "__main__":
    args = sys.argv[1:]  # Exclude the script name from arguments
    add_to_list_and_save(args)
