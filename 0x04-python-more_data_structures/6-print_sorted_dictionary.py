#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Print a dictionary by ordered keys."""
    for key, val in sorted(a_dictionary.items()):
        print("{}: {}".format(key, val))
