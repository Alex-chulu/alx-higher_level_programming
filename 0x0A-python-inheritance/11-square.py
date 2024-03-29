#!/usr/bin/python3
"""This is a class Square that inherits from Rectangle
    (9-rectangle.py)
    """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class

    Argus:
        Rectangle: parent class
    """
    def __init__(self, size):
        """Instantiation with size

        Args:
            size(int): size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns:
            str: square description
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))
