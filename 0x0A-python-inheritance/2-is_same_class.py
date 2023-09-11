#!/usr/bin/python3
"""
    function that returns True if the object is exactly an instance
    of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """Return true if object is an instance of the
    class, otherwise return false
    """
    return (type(obj) == a_class)
