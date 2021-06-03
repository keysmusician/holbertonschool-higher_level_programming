#!/usr/bin/python3
"""A class which extends a list."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Describe a square."""

    def __init__(self, size):
        """Initialize Square."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
