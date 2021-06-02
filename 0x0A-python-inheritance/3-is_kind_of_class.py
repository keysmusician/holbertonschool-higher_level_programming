#!/usr/bin/python3
"""A function which checks for a close class match."""


def is_same_class(obj, a_class):
    """Return whether an object is an instance of a class or subclass."""
    return isinstance(obj) == a_class
