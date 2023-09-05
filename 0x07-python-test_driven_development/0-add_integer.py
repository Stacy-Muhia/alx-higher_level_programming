#!/usr/bin/python3

"""
Adds two numbers
"""

def add_integer(a, b=98):
    """ Functions to add two integers
    Args:
        a: first number
        b: second number
    Returns:
        The addition of a and b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
