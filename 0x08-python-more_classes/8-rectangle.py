#!/usr/bin/python3

"""
    class that defines a rectangle
"""

class Rectangle:
    """class rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """private instance arrtribute of width and height"""
    
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

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
    def __str__(self):
        """
        print rectangle with a character
        """

        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""
        for x in range(self.__height):
            for y in range(self.__width):
                rectangle_str += str(self.print_symbol)

            rectangle_str += "\n"
        return rectangle_str[:-1]
    def __repr__(self):
        """
        return a string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
    def __del__(self):
        """
        for deletion
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
