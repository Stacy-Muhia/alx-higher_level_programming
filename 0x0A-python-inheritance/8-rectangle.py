#!/usr/bin/python3

"""an empty class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """define class attributes"""


    def __init__(self, width, height):
        """Intialize a new Rectangle."""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
