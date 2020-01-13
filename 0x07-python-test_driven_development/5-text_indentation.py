#!/usr/bin/python3

'''
This module contains the function
text_indentation(text) that
prints a text
'''


def text_indentation(text):

    '''
    This function prints a text with 2 new lines after  ., ? and :
    '''
    if type(text) is not str:
        raise TypeError('text must be a string')
    txt = text.replace(":", ":\n\n")
    txt = txt.replace("?", "?\n\n")
    txt = txt.replace(".", ".\n\n")
    words = txt.split("\n")

    for x in range(len(words)):
        print("{}".format(words[x].strip()),
              end=("" if (x == (len(words) - 1)) else '\n'))
