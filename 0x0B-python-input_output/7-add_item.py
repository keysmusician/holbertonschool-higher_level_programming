#!/usr/bin/python3
"""
Append command line arguments to a JSON list written in a file.

"""
if __name__ == "__main__":

    import json
    from sys import argv
    save_to_json = __import__('5-save_to_json_file').save_to_json_file
    load_from_json = __import__('6-load_from_json_file').load_from_json_file

    jsonlist = []
    with open("add_item.json", "a"):
        jsonlist = load_from_json("add_item.json")
    save_to_json(jsonlist + argv[1:], 'add_item.json')
