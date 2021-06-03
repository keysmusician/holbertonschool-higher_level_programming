#!/usr/bin/python3
"""A class which extends a list."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Describe a rectangle."""

    def __init__(self, width, height):
        """Initialize Rectangle."""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
