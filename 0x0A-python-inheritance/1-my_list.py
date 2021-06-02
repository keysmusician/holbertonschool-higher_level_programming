#!/usr/bin/python3
"""A class which extends a list."""


class MyList(list):
    """Add method to print this list sorted ascending without mutating self."""
    def print_sorted(self):
        """Print this list sorted ascending without mutating self."""
        print(sorted(self))
