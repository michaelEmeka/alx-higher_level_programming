#!/usr/bin/python3
"""Defines a class rectangle that inherits from base."""
from models.base import Base


class Rectangle(Base):
    """
    A rectangle class inheritting from Base class.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiates a Rectangle instance.
        Args:
            width: rectangle width.
            height: rectangle height.
            x: x coordinate.
            y: y coordinate.
            id: shape id.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(self, id)

    @property
    def width(self):
        """Set/get width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        """Set/get height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        """Set/get x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        """Set/get y coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
