#!/usr/bin/python3
"""
functions to print the fisrt and second name
"""

def say_my_name(first_name, last_name=""):
    """
        Write a function that prints My name is <first name> <last name>
        Args:
            first_name (str): the first string
            last_name (str): the second string
        Raises:
            TypeError: if name is not string
        Return: My name is <first name> <last name>
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
