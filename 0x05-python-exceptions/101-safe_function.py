#!/usr/bin/python3
from sys import stderr

def safe_function(fct, *args):
    """
    This function calls a function fct.

    Args:
        fct: a pointer to a function
        args: arguments for fct
    """
    a = int(args[0])
    b = int(args[1])
    try:
        ret = fct(a, b);
    except ZeroDivisionError as err:
        stderr.write("Exception: {}\n".format(err))
        ret = None

    return ret
