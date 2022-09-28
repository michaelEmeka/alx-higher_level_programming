#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    height = len(matrix)
    width = len(matrix[0])
    for row in range(height):
        for col in range(width):
            print("{:d}{}".format(matrix[row][col], " " if col + 1 != width else ""), end="")
        print()i
