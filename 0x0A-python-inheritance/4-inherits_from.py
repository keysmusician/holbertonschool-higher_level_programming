#!/usr/bin/python3
"""A function which checks for a class inheritance."""


def inherits_from(obj, a_class):
    """Return whether an object's class inherited from a class."""
    return False if type(obj) == a_class else issubclass(type(obj), a_class)
