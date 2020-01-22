#!/usr/bin/python3
"""
this module contains the function to_json_string
"""

import json


def to_json_string(my_obj):
    '''
    function that returns the JSON representation of an object (string)
    '''
    return json.dumps(my_obj)
