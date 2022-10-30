#!/usr/bin/python3
"""Defines a class: Student."""


class Student:
    """A Student calss."""
    def __init__(self, first_name, last_name, age):
        """
        Instantiates a Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student
        instance.
        Args:
            attrs: attributes needed in our dictionary.(optional).
        """
        if attrs is None:
            return self.__dict__
        if (type(attrs) == list and
                all(type(attr) == str for attr in attrs)):
            return {k: getattr(self, k) for k in attrs
                    if hasattr(self, k)}

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.
        Args:
            json: json dictionary(deserialized).
        """
        for k, v in json.items():
            setattr(self, k, v)
