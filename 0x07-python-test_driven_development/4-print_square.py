#!/usr/bin/python3

'''
This module contains the function

print_square(size)
'''


def print_square(size):

    '''
    This function prints a square with the character #
    '''
    sq = ''
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for x in range(size):
        sq += '#' * size + '\n'
    print(sq, end='')
