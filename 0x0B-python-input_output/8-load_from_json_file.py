#!/usr/bin/python3
'''
this module contains the function load_from_json_file
'''
import json


def load_from_json_file(filename=""):
    '''
    function that creates an Object from a “JSON file”
    '''
    with open(filename, encoding="utf-8") as f:
        obj_created = json.load(f)

    return obj_created
