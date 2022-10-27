#!/usr/bin/python3

"""Defones a class MyList."""


class MyList(list):
    """
    A class MyList that inherits from list.
    Args:
        list.
    """
    def print_sorted(self):
        """
        Prints sorted list.
        """
        print(sorted(self))
