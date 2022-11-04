#!/usr/bin/python3
"""Defines a square class that inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class."""
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiates a square."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Set/get square size."""
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = self.height = value
