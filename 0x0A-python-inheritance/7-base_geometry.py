#!/usr/bin/python3
"""This is a class BaseGeometry (based on 6-base_geometry.py)"""


class BaseGeometry:
    """A Base Geometry class
    """

    def area(self):
        """A public method that raises an Exception
        with the message 'area() is not implemented.'
        
        Raises:
            Exception: [area() is not implemented]
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A public instance method that validates value

        Args:
            name(str): name
            value(int): value contained

        Raises:
            TypeError: 'name must be an integer'
            ValueError: 'name must be greater than 0'
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
