#!/usr/bin/python3
"""Defines a rebel class."""


class MyInt(int):
    """
    A rebel class(has == and != operators inverted).
    """
    def __eq__(self, value):
        """
        Overrides == operator with != behavior.
        Args:
            value: int instance.
        """
        return self.real != value

    def __ne__(self, value):
        """
        Overrides != operator with == behavior.
        Args:
            value: int instance.
        """
        return self.real == value
