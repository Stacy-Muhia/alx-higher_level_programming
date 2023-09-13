#!/usr/bin/python3

"""
   function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
       prints the contents of the text file read to stdout
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
