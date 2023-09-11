#!/usr/bin/python3

"""an empty clas"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """define class attributes"""
    def __init__(self, width, height):
        """Intialize a new Rectangle."""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """calculate the area"""
        return self.__width * self.__height

    def __str__(self):
        """return, the following rectangle description:"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
