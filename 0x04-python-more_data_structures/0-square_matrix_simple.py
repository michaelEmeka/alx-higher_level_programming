#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr_matrix = matrix.copy()
    for i in range(len(matrix)):
        sqr_matrix[i] = [x**2 for x in matrix[i]]
    return sqr_matrix
