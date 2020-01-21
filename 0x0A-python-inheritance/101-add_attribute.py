#!/usr/bin/python3

"""
this module contains add_attribute function
"""


def add_attribute(objec, attribute, value):
    """
    function that adds a new attribute to an object
    """
    if hasattr(objec, "__dict__"):
        setattr(objec, attribute, value)
    else:
        raise TypeError("can't add new attribute")
