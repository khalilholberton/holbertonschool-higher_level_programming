#!/usr/bin/python3

'''
This module contains the function
def matrix_divided(matrix, div) and accept two
arguments matrix and div
'''


def matrix_divided(matrix, div):
    '''
    This function divides all elements of a matrix by div
    '''
    new_matrix = []
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(error_msg)
    for block in matrix:
        if type(block) is not list:
            raise TypeError(error_msg)
    for block in matrix:
        if len(matrix[0]) != len(block):
            raise TypeError("Each row of the matrix must have the same size")
    for block in matrix:
        for token in block:
            if not isinstance(token, (int, float)):
                raise TypeError(error_msg)
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for block in matrix:
        new_block = []
        for token in block:
             new_block.append( round((token / div), 2))
        new_matrix.append(new_block)
    return new_matrix
