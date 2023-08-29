#!/usr/bin/python3
"""used to def a class Square."""


class Square:
    """defines a square."""

    def __init__(self, size=0):
        """Int a new Square.
        Args:
            size (int): The specific size of the object  new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
