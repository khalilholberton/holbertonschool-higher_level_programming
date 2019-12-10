#!/usr/bin/python3
def remove_char_at(str, n):
    string = ""
    count = len(str)
    for x in range(count):
        if x != n:
            string = strr + str[x]
    return(string)
