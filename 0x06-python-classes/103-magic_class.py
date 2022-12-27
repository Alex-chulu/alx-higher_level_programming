#!/usr/bin/python3

"""Defining MagicClass matching bytecode provided"""

import math


class MagicClass:
    """Representint a circle"""

    def __init__(self, radius=0):
        """Initializing a MagicClass

        Arg:
            radius (float or int): Radius of the new MagicClass
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returning area of the MagicClass"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Returning circumference of the MagicClass"""
        return (2 * math.pi * self.__radius)
