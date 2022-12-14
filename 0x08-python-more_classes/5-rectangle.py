#!/usr/bin/python3
"""Defines Class Rectangle."""


class Rectangle:
    """Represents rectangle."""

    def __init__(self, width=0, height=0):
        """Initialized Rectangle.

        Args:
            width (int): Rectangle width.
            height (int): Rectangle height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get Rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get Rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return Rectangle Area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return Rectangle Perimeter."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable Rectangle represantation.

        Using # to represent rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []
        for y in range(self.__height):
            [rectangle.append('#') for j in range(self.__width)]
            if y != self.__height - 1:
                rectangle.append("\n")
        return ("".join(rectangle))

    def __repr__(self):
        """Returnstring representation of the Rectangle."""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return (rectangle)

    def __del__(self):
        """Print out message for any deletion occurency of Rectangle."""
        print("Bye rectangle...")
