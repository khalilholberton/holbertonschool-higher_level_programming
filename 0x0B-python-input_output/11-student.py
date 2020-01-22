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
        initialization of the variables
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''
        return dict representation
        '''
        return (self.__dict__)
