#!/usr/bin/python3

""" creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """
       function that creates an Object from a JSON file

       must use the with statement

       don’t need to manage exceptions if the JSON string doesn’t represent an object.

       don’t need to manage file permissions / exceptions.
    """
    with open(filename) as f:
        return json.load(f)
