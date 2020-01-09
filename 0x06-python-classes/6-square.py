#!/usr/bin/python3


class Square:

    '''
    definition of square class
    '''
    def __init__(self, size=0, position=(0, 0)):

        '''
        initialization of square instance
        '''
        error_message = "position must be a tuple of 2 positive integers"
        if ((type(position) is not tuple) or (len(position) != 2)) \
            or (type(position[0]) is not int) \
            or (type(position[1]) is not int) \
                or ((position[0] < 0) or (position[1] < 0)):
            raise TypeError(error_message)
        elif type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        '''
        defining the square position

        '''
        return(self.__position)

    @position.setter
    def position(self, value):

        '''
        defining position setter

        '''
        error_msg = "position must be a tuple of 2 positive integers"
        if ((type(value) is not tuple) or (len(value) != 2)) \
            or (type(value[0]) is not int) \
            or (type(value[1]) is not int) \
                or ((value[0] < 0) or (value[1] < 0)):
            raise TypeError(error_msg)

    def my_print(self):
        '''
        print in stdout the square with character # or blank line if 0
        '''
        if self.__size == 0:
            print()
        else:
            for x in range(self.__position[1]):
                print()
            for y in range(self.__size):
                for z in range(self.__position[0]):
                    print(" ", end="")
                for w in range(self.__size):
                    print("#", end="")
                print()
