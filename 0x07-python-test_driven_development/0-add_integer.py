#!/usr/bin/python3
"""
Add Integer

This module supplies one function, add_integer().

Usage:

>>> add_integer(5, 6)
11

"""


def add_integer(a, b=98):
    """Return the sum of two integers.

    >>> add_integer(2, 3)
    5
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
