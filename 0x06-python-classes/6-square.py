#!/usr/bin/python3

"""Defines a class Square."""


class Square:
    """A Square class."""
    def __init__(self, size=0, position=(0, 0)):
        """
        Instantiates a square class.
        Args:
            size: A square's size.
        """
        self.__size = size
        if (not isinstance(position, tuple)
                or not all(isinstance(num, int) for num in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (not all(num >= 0 for num in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """
        Retrieve square's size private instance attribute.
        Returns: size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets a square's size private attribute.
        Args:
            value: square's size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        Retrieves square's position.
        Returns: position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets a square's position private attribute.
        Args:
        value: square's position.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__postion = value

    def area(self):
        """
        Returns: Area of square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints a square.
        """
        lb = self.__size
        pos = self.__position
        if lb == 0:
            print()
        else:
            for y in range(pos[1]):
                print("")
            for i in range(lb):
                for x in range(pos[0]):
                    print(" ", end="")
                for j in range(lb):
                    print("#", end="")
                print()
