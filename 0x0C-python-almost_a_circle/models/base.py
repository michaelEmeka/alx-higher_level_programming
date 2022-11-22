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

    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of
        list_dictionaries.
        """
        return (json.dumps(list_dictionaries))
