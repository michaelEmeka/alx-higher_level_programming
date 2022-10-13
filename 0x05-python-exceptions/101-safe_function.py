#!/usr/bin/python3
from sys import stderr

def safe_function(fct, *args):
    """
    This function calls a function fct.

    Args:
        fct: a pointer to a function
        args: arguments for fct
    """
    a = args[0]
    b = args[1]
    try:
        ret = fct(a, b);
    except Exception as err:
        stderr.write("Exception: {}\n".format(err))
        ret = None

    return ret
