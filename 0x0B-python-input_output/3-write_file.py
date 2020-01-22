#!/usr/bin/python3
'''
this module contains the function write_file
'''


def write_file(filename="", text=""):
    '''
    function to write to files
    '''
    with open(filename, mode="w") as f:
        words = f.write(text)
    return words
