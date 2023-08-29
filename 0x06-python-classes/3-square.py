#!usr/bin/python3

class Square:
    """define the self values"""
    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        """declare the self value to size"""
        self.__size = size

    """states  the method to find area"""
    def area(self):
        return (self.__size ** 2)
