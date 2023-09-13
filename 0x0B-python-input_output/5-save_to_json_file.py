#!/usr/bin/python3

"""writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """
        writes an Object to a text file, using a JSON representation
        
        must use the with statement

        don’t need to manage exceptions and file permission exceptions
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
