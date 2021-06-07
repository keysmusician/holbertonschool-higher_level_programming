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

    def update(self, *args, **kwargs):
        """Update attributes."""
        if len(args):
            # Set default values for attributes
            new_vals = [self.id, self.size, self.x, self.y]
            # Replace default values with values provided from 'args', if any
            for i, arg in enumerate(args):
                new_vals[i] = arg
            self.id, self.size, self.x, self.y = new_vals
        else:
            for attr, value in kwargs.items():
                if hasattr(self, attr):
                    setattr(self, attr, value)
