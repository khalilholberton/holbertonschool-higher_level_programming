#!/usr/bin/python3
'''
this module contains the function class_to_json
'''


def class_to_json(obj):
    '''
    returns the dictionary description
    '''
    return obj.__dict__
