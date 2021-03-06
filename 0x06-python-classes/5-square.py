#!/usr/bin/python3


class Square:

    '''
    definition of square class
    '''
    def __init__(self, size=0):

        '''
        initialization of square instance
        '''
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        '''
        return the square area
        '''
        return (self.__size ** 2)

    @property
    def size(self):
        '''
        defining square size and return the value
        '''
        return(self.__size)

    @size.setter
    def size(self, value):
        '''
        defining the square size
        '''
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        '''
        print in stdout the square with character # or blank line if 0

        '''
        if self.size == 0:
            print()
            return
        for x in range(self.__size):
            for y in range(self.__size):
                print('#', end="")
            print()
