#!/usr/bin/python3
"""A class definition of a rectangle"""

class Rectangle:
    """A rectangle."""
    def __init__(self, width=0, height=0):
        """Create a new rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width of this rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of this rectangle."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height of this rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of this rectangle."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__height = value
