#!/usr/bin/python3

'''
This module contains the class Rectangle
'''


class Rectangle:
    '''defines the Rectangle'''
    def __init__(self, width=0, height=0):
        '''
         initialize height and width
        '''
        self.height = height
        self.width = width

    @property
    def width(self):
        '''
            Return width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''
        fonction raise TypeError and ValueError and set width
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''
         return height
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
         function raise TypeError and ValueError and set the height
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''
        return the area of a rectangle
        '''
        return self.height * self.width

    def perimeter(self):
        '''
        return the perimeter of a rectangle
        '''
        if self.height == 0 or self.width == 0:
            return 0

        return (self.height + self.width) * 2
