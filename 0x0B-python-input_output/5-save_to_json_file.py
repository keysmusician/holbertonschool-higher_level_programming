#!/usr/bin/python3
"""A function that writes an object to a text file in JSON format."""


import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file in JSON format."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
