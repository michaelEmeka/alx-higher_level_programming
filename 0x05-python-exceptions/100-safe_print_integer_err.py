#!/usr/bin/python3
from sys import stderr
def safe_print_integer_err(value):
    """Prints an integer using {:d}.format.

    Args:
        value: value to be printed.

    Return:
        True, if value passed is of integer type
        and has successfully been printed.
        False,on failure.
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as err:
        stderr.write("Exception: {}".format(err))
        return False
