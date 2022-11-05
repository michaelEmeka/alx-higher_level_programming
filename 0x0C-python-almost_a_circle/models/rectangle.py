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
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Set/get height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Set/get x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Set/get y coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area of triangle."""
        return (self.__width * self.__height)

    def display(self):
        """Prints a grid of harshes "#" tho represent
        the shape"""
        w = h = x = y = 0
        for y in range(self.__y):
            print()
        while h < self.__height:
            while x < self.__x:
                print(" ", end="")
                x += 1
            while w < self.__width:
                print("#", end="")
                w += 1
            print()
            w = x = 0
            h += 1

    def __str__(self):
        """Overides the __str__ method so it prints
        [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        message = "[{}] ".format(self.__class__.__name__)
        message += "({}) ".format(self.id)
        message += "{}/{} - ".format(self.__x, self.__y)
        if self.__width != self.__height:
            message += "{}/{}".format(self.__width, self.__height)
        else:
            message += "{}".format(self.__width)
        return message

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute.
        Args:
            *args: list of attribute values.
            **kwargs: kew word arguments.
        """
        if (args is not None) and (len(args) != 0):
            att = ["id", "width", "height", "x", "y"]
            for v in range(len(args)):
                setattr(self, att[v], args[v])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary representation of an
        instance."""
        return self.__dict__
