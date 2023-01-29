#!/usr/bin/python3
"""This is a class Rectangle that inherits from
    BaseGeometry (7-base_geometry.py)."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherits from BaseGeometry

    Args:
        BaseGeometry: Super class
    """
    def __init__(self, width, height):
        """
        Args:
            width (int): must be private and positive integers. No getter or setter
            height (int): must be private and positive integers. No getter or setter
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
