#!/usr/bin/python3
"""A class definition of a rectangle"""


class Rectangle:
    """Define a rectangle."""

    def __init__(self, width=0, height=0):
        """Create a new rectangle"""
        self.width = width
        self.height = height

    def __str__(self):
        """Represent this rectangle with '#' characters."""
        if self.width == 0 or self.height == 0:
            return ''
        return ((self.width * '#' + '\n') * self.height)[:-1]

    def __repr__(self):
        """Return a string that will construct this rectangle if called."""
        return "{:s}({:d},{:d})".format(
            type(self).__name__, self.width, self.height)

    @property
    def width(self):
        """Get width of this rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of this rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height of this rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of this rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Get area of this rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Get perimeter of this rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * self.width + 2 * self.height
