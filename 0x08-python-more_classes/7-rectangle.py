#!/usr/bin/python3
"""A class definition of a rectangle"""


class Rectangle:
    """Define a rectangle."""

    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Create a new rectangle"""
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    def __str__(self):
        """Represent this rectangle with the 'print_symbol' class attribute."""
        if self.width == 0 or self.height == 0:
            return ""
        symbol = str(self.print_symbol)
        row = (self.width * symbol + "\n")
        return (row * self.height)[:-1]

    def __repr__(self):
        """Return a string that will construct this rectangle if called."""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """Delete this rectangle."""
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")

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


my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
print("--")
my_rectangle_1.print_symbol = "&"
print(my_rectangle_1)
print("--")

my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)
print("--")
Rectangle.print_symbol = "C"
print(my_rectangle_2)
print("--")

my_rectangle_3 = Rectangle(7, 3)
print(my_rectangle_3)

print("--")

my_rectangle_3.print_symbol = ["C", "is", "fun!"]
print(my_rectangle_3)

print("--")
