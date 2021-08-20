#!/usr/bin/python3
"""A function which identifies peaks in a list of numbers."""


def find_peak(list_of_integers):
    """Find a peak in a list of integers."""
    try:
        return sorted(list_of_integers)[-1]
    except:
        return None
