#!/usr/bin/python3

def matrix_divided(matrix, div):

    """
    This function divides a matrix(list of lists).

    Args:

        matrix: a list of lists.
        div: divisor.

    Returns: a new matrix of divided values.
    """
    """
        Check for matrix type.
        Check if matrix contains lists.
        Saves each size.
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    for l in matrix:
        if not isinstance(l, list):
            raise TypeError("matrix must be a list of lists")
        
