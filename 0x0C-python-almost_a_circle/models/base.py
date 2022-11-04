#!/usr/bin/python3
"""Defines a class named base."""


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