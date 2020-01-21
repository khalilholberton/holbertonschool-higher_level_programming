#!/usr/bin/python3

'''
this module contain Mylist class
'''


class MyList(list):
    '''
        Prints a sorted list
    '''
    def print_sorted(self):
        print(sorted(self))
