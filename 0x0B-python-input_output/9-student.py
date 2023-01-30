#!/usr/bin/python3
"""Student class that defines a student"""


class Student:
    """ Student class """

    def __init__(self, first_name, last_name, age):
        """Initializing class

        Args:
            first_name: Student first name
            last_name: Student last name
            age: Student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance

        Returns:
            dictionary representation of a Student instance
        """
        return self.__dict__
