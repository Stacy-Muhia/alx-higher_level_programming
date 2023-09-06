#!/usr/bin/python3

"""
    class that defines a rectangle
"""


class Rectangle:
    """class rectangle"""

    def __init__(self, width=0, height=0):
        """private instance arrtribute of width and height"""
    
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        defines the attribute width of the rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        this is what sets the width
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        defines the attribute height of the rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        this stes the value of heeight
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        the area of our rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        the perimeter of our rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2
