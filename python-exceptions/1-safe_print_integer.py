#!/usr/bin/python3


def safe_print_integer(value):
    """Prints an integer with "{:d}".format() and returns True if successful."""
   try:
        print("{:d}".format(value))  # Attempt to format and print the value as an integer
        return True                   # Return True if the operation was successful
    except (ValueError, TypeError):   # Catch ValueError and TypeError
        return False      
