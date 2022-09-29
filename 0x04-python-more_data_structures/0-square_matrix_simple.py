#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr_mtrix = matrix.copy()
    j = 0
    for i in matrix:
        sqr_mtrix[j] = [x**2 for x in i]
        j = j + 1
        return sqr_mtrix
