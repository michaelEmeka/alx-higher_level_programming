#!/usr/bin/python3
"""Defines a class named base."""
import json


class Base:
    """Base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiates a class.
        Args:
            id: instance id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of
        list_dictionaries if it is not None.
        else: "[]" string.
        """
        if list_dictionaries is not None:
            return (json.dumps(list_dictionaries))
        return "[]"

    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs
        to a file.
        """
        filename = list_objs[0].__class__.__name__ + ".json"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(to_json_string)
