#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A simple class definition describing a square."""


class Square:
    """Create a square."""

    def __init__(self, size=0):
        """Initialize a Square object.

        Args:
            size (int): A positive integer as the size of the new square.
        """
        self.__size = size

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): A positive integer as the size of the new square.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
