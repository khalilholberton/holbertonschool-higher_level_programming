#!/usr/bin/python3
'''
this module contains the function number_of_lines
'''


def number_of_lines(filename=""):
    '''
     returns the number of lines in a file
    '''
    l_num = 0

    with open(filename, encoding="utf-8") as f:
        for line in f:
            l_num += 1
    return l_num
