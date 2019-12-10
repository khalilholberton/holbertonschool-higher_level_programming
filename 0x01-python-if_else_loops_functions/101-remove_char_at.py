#!/usr/bin/python3
def remove_char_at(str, n):
    str = ""
    c = 0
    for x in str:
        if (c != n):
            str = str + x
        c = c + 1
    return(str)
