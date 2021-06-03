#!/usr/bin/python3
"""Class 'Student' that defines a student."""


class Student:
    """Define a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve dictionary representation of self."""
        return self.__dict__
