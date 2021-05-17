#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Safely print an integer."""
    try:
        print("{:d}".format(value))
        return True
    except:
        sys.stderr.write("Exception: {}\n".format(sys.exc_info()[1]))
    return False
