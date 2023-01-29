#!/usr/bin/python3AOA
"""This is class Rectangle that inherits from BaseGeometry
    (7-base_geometry.py).
    """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class that inherits from Base class

    Args:
        BaseGeometry: super class
    """
    def __init__(self, width, height):
        """width and height instantiating

        Args:
            width: must be private and positve integer. No getter or setter
            height: must be private and positve integer. No getter or setter
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area, method to be implemented

        Returns:
            Area(int): area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """string

        Returns:
            string(str): rectangle description
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
