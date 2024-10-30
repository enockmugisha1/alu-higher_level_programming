#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count = 0  # To count the number of elements printed
    for i in range(x):  # We will attempt to print x elements
        try:
            print(my_list[i], end='')  # Print the element without a newline
            count += 1  # Increment the count of printed elements
        except IndexError:
            break  # Stop trying to print if we run out of elements
    print()  # Print a newline after printing the elements
    return count  # Return the number of elements printed
