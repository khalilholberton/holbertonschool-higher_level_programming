#!/usr/bin/python3
def remove_char_at(str, n):
    st = ""
    c = 0
    for x in str:
        if (c != n):
            st = st + x
        c = c + 1
    return(st)
