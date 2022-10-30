#!/usr/bin/python3
"""Defines a class: Student."""


class Student:
    """
    Defines a Student.
    """
    def __init__(self, first_name, last_name, age):
        """Instantiates a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a student
        instance.
        """
        if attrs == None:
            return self.__dict__
        if (type(attrs) == list and
                all(type(attr) == str for attr in attrs)):
            return {k: getattr(self, k) for k in attrs
                    if hasattr(self, k)}
