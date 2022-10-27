#!/usr/bin/python3

"""Defones a class MyList."""


class MyList(list):
    """
    A class MyList that inherits from list.
    Args:
        list.
    """
    def __init__(self):
    """
    Instantiation.
    """
        list.__init__(self)
    def print_sorted(self):
        """
        Prints sorted list.
        """
        p = self.copy()
        p.sort()
        print(p)
