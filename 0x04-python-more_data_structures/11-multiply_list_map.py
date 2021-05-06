#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """Return a list of values multiplied by 'number' without using loops."""
    return list(map(lambda x: x * number, my_list))
