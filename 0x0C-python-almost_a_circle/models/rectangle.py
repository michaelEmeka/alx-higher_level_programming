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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        Base.__init__(self, id)

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def width(self):
        return self.__width

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def height(self):
        return self.__height

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def x(self):
        return self.__x

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def y(self):
        return y
