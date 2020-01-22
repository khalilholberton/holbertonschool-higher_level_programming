#!/usr/bin/python3
'''
this module contain the function append_write
'''


def append_write(filename="", text=""):
    '''
    function that appends a string at the end of a text file
    '''
    with open(filename, mode="a", encoding='utf-8') as f:
        words = f.write(text)
    return words
