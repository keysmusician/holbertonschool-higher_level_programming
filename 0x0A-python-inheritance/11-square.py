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


class Rectangle(BaseGeometry):
    """Describe a rectangle."""

    def __init__(self, width, height):
        """Initialize Rectangle."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """Text description of Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Calculate area of Rectangle."""
        return self.__width * self.__height


class Square(Rectangle):
    """Describe a square."""

    def __init__(self, size):
        """Initialize Square."""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculate area of Square."""
        return self.__size ** 2

    def __str__(self):
        return "[Square] {size}/{size}".format(size=self.__size)
