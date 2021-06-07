#!/usr/bin/python3
"""
Rectangle class definition.

"""


from .base import Base


class Rectangle(Base):
    """Define a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize rectangle."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Return width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Return height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Return x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Return y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __str__(self):
        """Display basic information."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def area(self):
        """Return area."""
        return self.width * self.height

    def display(self):
        """Print rectangle in text."""
        y_offset = '\n' * self.y
        x_offset = ' ' * self.x
        row = (x_offset + '#' * self.width + '\n')
        text_rectangle = y_offset + (row * self.height)
        # Remove trailing newline
        print(text_rectangle[:-1])

    def update(self, *args):
        """Update attributes."""
        # Set default values for attributes
        new_args = [self.id, self.width, self.height, self.x, self.y]
        # Replace default values with values provided from 'args'
        for i, arg in enumerate(args):
            new_args[i] = arg

        self.id, self.width, self.height, self.x, self.y = new_args
