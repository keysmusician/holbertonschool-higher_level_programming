#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""A simple class definition describing a square."""


class Square:
    """Create a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square object.

        Args:
            size (int): A positive integer as the size of the new square.
            position (tuple): A pair of positive integers describing a
                positional offset.
        """
        self.size = size
        self.position = position

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square at '__position' with '#'."""
        if self.__size == 0:
            print()
            return
        print("\n" * self.__position[1], end='')
        for row in range(self.__size):
            print(' ' * self.__position[0], end='')
            print("#" * self.__size)

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

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

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): Value to represent position must be a tuple of two
                positive integers.
        """
        if type(value) is tuple and\
                len(value) == 2 and\
                type(value[0]) is int and\
                type(value[1]) is int and\
                value[0] >= 0 and\
                value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
