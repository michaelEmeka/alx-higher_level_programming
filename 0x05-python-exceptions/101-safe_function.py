#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    """
    This function calls a function fct.

    Args:
        fct: a pointer to a function
        args: arguments for fct
    """
    try:
        ret = fct(*args)
    except Exception as err:
        stderr.write("Exception: {}\n".format(err))
        ret = None

    return ret
