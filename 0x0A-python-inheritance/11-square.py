#!/usr/bin/python3
'''
this module contains Square class
'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    class Square
    '''
    def __init__(self, size):
        '''
        instanciation of the class
        '''
        super().integer_validator(size, size)
        super().__init__(size, size)
        self.size = size

    def area(self):
        '''
        return the area
        '''
        return self.size ** 2

    def __str__(self):
        '''
        string representation
        '''
        return "[Square] {}/{}".format(self.size, self.size)
