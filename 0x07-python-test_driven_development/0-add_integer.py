#!/usr/bin/python3

'''
This module contains the function
add_integer(a, b) that adds two integers
'''


def add_integer(a, b=98):
    '''
    This function return the sum of two integers , cast arguments to int
    if a or b is float
    '''
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
