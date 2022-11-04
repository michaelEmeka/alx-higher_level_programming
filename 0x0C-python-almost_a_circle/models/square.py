#!/usr/bin/python3
"""Defines a square class that inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class."""
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiates a square."""
        super().__init__(size, size, x, y, id)
