#!/usr/bin/python3
"""
Add all command line arguments to a Python list, and append them to a file.

"""


import json
import sys


def save_to_json_file(my_obj, filename):
    """Write an object to a text file in JSON format."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """Create an object from a JSON file."""
    with open(filename, "r") as file:
        return json.load(file)


with open('add_item.json', 'r') as file:
    json_list = load_from_json_file('add_item.json')
    print(json_list)
with open('add_item.json', 'w') as file:
    json.dump(json_list + sys.argv[1:], file)
