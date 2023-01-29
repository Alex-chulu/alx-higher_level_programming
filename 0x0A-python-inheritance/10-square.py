#!/usr/bin/python3
"""This is a Square class that inherits from Rectangle
    (9-rectangle.py)
    """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class

    Args:
        Rectangle: super class
    """
    def __init__(self, size):
        """Instantiation with size

        Args:
            size(int): size of the square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """area, method that must be implented

        Returns:
            area(int): area of rectangle
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns:
            string(str): rectangle description
        """
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
