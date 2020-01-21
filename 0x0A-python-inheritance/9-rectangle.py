#!/usr/bin/python3
'''
    this module contains the class Rectangle
'''
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    '''
     class  Rectangle
    '''
    def __init__(self, width, height):
        '''
        instanciate the Rectangle class
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        '''
        return area of the rectangle
        '''
        return (self.__width * self.__height)

    def __str__(self):
        '''
        Rectangle class string representation
        '''
        return ("[{}] {}/{}"
                .format(type(self).__name__, self.__width, self.__height))
