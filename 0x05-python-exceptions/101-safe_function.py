#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Safely execute a function."""
    try:
        return fct(*args)
    except:
        sys.stderr.write("Exception: {}\n".format(sys.exc_info()[1]))
        return None
