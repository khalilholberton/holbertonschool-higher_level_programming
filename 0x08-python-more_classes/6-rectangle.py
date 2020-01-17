#!/usr/bin/python3

'''
This module contains the class Rectangle
'''


class Rectangle:
    '''defines the Rectangle'''
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        '''
         initialize height and width
        '''
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        '''
        returns the string representation
        '''
        rec = ''
        if self.__height == 0 or self.__width == 0:
            return rec
        size_h = self.__height
        size_w = self.__width
        for x in range(size_h):
            for y in range(size_w):
                rec += '#'
            rec += "\n"
        return rec[:-1]

    def __repr__(self):
        '''returns a string of generating new object'''
        return ('Rectangle({}, {})'.format(self.__width, self.height))

    def __del__(self):
        ''' prints message when instance is deleted'''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
