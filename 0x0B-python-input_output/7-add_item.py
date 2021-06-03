#!/usr/bin/python3
"""
Add all command line arguments to a Python list, and append them to a file.

"""


import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


with open('add_item.json', 'r') as file:
    json_list = load_from_json_file('add_item.json')
    print(json_list)
with open('add_item.json', 'w') as file:
    json.dump(json_list + sys.argv[1:], file)
