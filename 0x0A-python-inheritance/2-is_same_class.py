#!/usr/bin/python3
"""A function which checks for an exact class match."""


def is_same_class(obj, a_class):
    """Return whether an object is exactly an instance of a class"""
    return type(obj) == a_class
