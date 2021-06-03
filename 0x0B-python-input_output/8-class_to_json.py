#!/usr/bin/python3
"""
A function that returns an object's dictionary
(useful for JSON serialization).

"""


def class_to_json(obj):
    """Return the dictionary of 'obj'."""
    return obj.__dict__
