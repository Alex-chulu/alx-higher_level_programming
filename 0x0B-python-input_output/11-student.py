#!/usr/bin/python3
"""Student class that defines a student by: (based on 10-student.py)"""


class Student:
    """
        Student class
    """
    def __init__(self, first_name, last_name, age):
        """initializing a class

        Args:
            first_name: Student fir st name
            last_name: Student last name
            age: Student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance.

        Returns:
            dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        dictionary = {}
        for attr in attrs:
            if attr in self.__dict__:
                dictionary[attr] = self.__dict__[attr]
        return dictionary

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance

        Args:
            json: a dictionary
        """
        dictionary = dict(json)
        for key in dictionary:
            self.__dict__[key] = dic[key]
