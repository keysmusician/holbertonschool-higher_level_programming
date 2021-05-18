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
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
