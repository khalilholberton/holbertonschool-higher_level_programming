#!/usr/bin/python3
'''
this module contain the class BaseGeometry
'''


class BaseGeometry:
    '''
    class BaseGeometry
    '''
    def area(self):
        '''
        Calculatesthe area
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
            Validating the value
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
