#!/usr/bin/python3
'''
this module contains the class Student
'''


class Student:
    '''
    class Student
    '''
    def __init__(self, first_name, last_name, age):
        '''
        initializiation of the variables
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        return dict representation
        '''
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for elements in attrs:
            if hasattr(self, elements):
                new_dict[elements] = getattr(self, elements)
        return (new_dict)
