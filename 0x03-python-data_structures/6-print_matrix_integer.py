#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in range(len(matrix)):
        space = ""
        for y in range(len(matrix[x])):
            print(space, end="")
            print("{:d}".format(matrix[x][y]), end="")
            space = " "
        print()
