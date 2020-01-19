#!/usr/bin/python3

'''
This module contains the class Rectangle
'''


class Rectangle:
    '''defines the Rectangle'''
    number_of_instances = 0
    print_symbol = "#"

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
        return self.__height * self.__width

    def perimeter(self):
        '''
        return the perimeter of a rectangle
        '''
        if self.__height == 0 or self.__width == 0:
            return 0

        return (self.__height + self.__width) * 2

    def __str__(self):
        '''
        returns the string representation
        '''
        sym = str(self.print_symbol)
        rec = ''
        if self.__height == 0 or self.__width == 0:
            return rec
        size_h = self.__height
        size_w = self.__width
        for x in range(size_h):
            for y in range(size_w):
                rec += sym
            rec += "\n"
        return rec[:-1]

    def __repr__(self):
        '''returns a string of generating new object'''
        return ('Rectangle({}, {})'.format(self.__width, self.height))

    def __del__(self):
        ''' prints message when instance is deleted'''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        '''return the biggest rectangle camparing the area'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        ''' return new rect instance where height and width =  size'''
        return cls(size, size)
