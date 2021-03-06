#!/usr/bin/python3
'''
this module contains Square class
'''
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''
    Square class
    '''
    def __init__(self, size):
        '''
        instanciation of the class
        '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return (self.__size ** 2)
