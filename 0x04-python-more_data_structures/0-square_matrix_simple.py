#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if (matrix):
        new_mat = []
        for line in matrix:
            new_mat.append(list(map(lambda x: x * x, line)))
        return new_mat
