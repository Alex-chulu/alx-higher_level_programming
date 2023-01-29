#!/usr/bin/python3
"""This is class BaseGeometry (based on 5-base_geometry.py)"""


class BaseGeometry:
    """
    public method: that raises an Exception with
    the message area() is not implemented
    """
    def area(self):
        raise Exception("area() is not implemented")
