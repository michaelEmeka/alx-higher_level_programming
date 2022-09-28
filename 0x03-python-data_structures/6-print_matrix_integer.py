#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    height = len(matrix)
    width = len(matrix[0])
    for row in range(height):
        for col in range(width):
            print("{:d}".format(matrix[row][col]), end="")
            if col + 1 != width:
                print("{}".format(" "), end="")
            else:
                print("{}".format(""), end="")
        print()
