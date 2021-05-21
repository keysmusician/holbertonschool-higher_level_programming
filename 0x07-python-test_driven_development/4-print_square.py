#!/usr/bin/python3
"""
A function which prints a square.

"""


def print_square(size):
    """Print a square of size 'size'"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for col in range(size):
        print("#" * size)
