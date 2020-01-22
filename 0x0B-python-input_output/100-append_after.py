#!/usr/bin/python3
'''
this module contains the function append_after
'''


def append_after(filename="", search_string="", new_string=""):
    '''
    inserts a lineto a file after each line containing a specific string
    '''
    mystring = ""
    with open(filename, encoding="utf8") as f:
        for line in f:
            mystring = mystring + line
            if search_string in line:
                mystring = mystring + new_string

    with open(filename, mode="w") as f:
        f.write(mystring)
