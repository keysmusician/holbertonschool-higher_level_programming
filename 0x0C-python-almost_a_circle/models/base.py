#!/usr/bin/python3
"""
Base class for project 0x0C. Python - Almost a circle

"""


class Base:
    """Define a base class to manage the 'id' attribute in derived classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize base class object."""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
