#!/usr/bin/python3
"""Student class that defines a student by: (based on 9-student.py"""


class Student:
    """
        Student class
    """
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

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance

        Returns:
            Dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        dictionart = {}
        for attr in attrs:
            if attr in self.__dict__:
                dictionary[attr] = self.__dict__[attr]
        return dictionart
