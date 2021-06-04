#!/usr/bin/python3
"""Class 'Student' that defines a student."""


class Student:
    """Define a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dictionary representation of self.

        Return: If attribute names are provided as a list of strings, returns
        only the dictionary containing only the specified attributes. Other-
        wise, returns the entire dictionary.

        """
        if type(attrs) is list and all([type(s) is str for s in attrs]):
            return {k: v for (k, v) in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of self."""
        self.__dict__ = json
