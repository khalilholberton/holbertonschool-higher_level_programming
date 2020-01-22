#!/usr/bin/python3
'''this module contains the function read_lines'''


def read_lines(filename="", nb_lines=0):
    '''
    function that reads n lines of a text file (UTF8) and prints it to stdout
    '''
    counter = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            counter += 1
            print(line, end="")
            if nb_lines == counter:
                break
