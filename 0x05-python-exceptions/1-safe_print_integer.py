#!/usr/bin/python3


def safe_print_integer(value):
    """Safely print an integer with the format method."""
    try:
        print("{:d}".format(value))
        return True
    except:
        return False
