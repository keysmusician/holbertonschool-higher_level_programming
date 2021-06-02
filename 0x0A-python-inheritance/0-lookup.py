#!/usr/bin/python3
"""A function to lookup object attributes."""


def lookup(obj):
    """Return a list of available attributes of 'obj'."""
    return dir(obj)
