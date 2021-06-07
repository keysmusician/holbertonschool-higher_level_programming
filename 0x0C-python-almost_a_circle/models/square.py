#!/usr/bin/python3
"""
Square class definition.

"""


from .rectangle import Rectangle


class Square(Rectangle):
    """Define a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize square."""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Display basic information."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Return size."""
        return self.width

    @size.setter
    def size(self, value):
        """Set size."""
        self.width = value
        self.height = value
