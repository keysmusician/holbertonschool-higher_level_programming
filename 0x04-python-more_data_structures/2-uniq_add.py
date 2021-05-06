#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Add all unique integers in a list (only once for each integer)."""
    return sum({n for n in my_list})
