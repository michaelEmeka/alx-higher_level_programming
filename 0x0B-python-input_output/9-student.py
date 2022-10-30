#!/usr/bin/python3
"""Defines a clss Student."""


class Student:
    """Defines a student instance."""
    def __init__(self, first_name, last_name, age):
        """Instantiates a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student
        instance.
        """
        return self.__dict__
