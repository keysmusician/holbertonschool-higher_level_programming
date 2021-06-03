#!/usr/bin/python3
"""A class which extends a list."""


class BaseGeometry:
    """Describe basic geometric shapes."""

    def area(self):
        """Placeholder area function."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Ensure values are positive integers."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
