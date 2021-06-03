#!/usr/bin/python3
"""
Append command line arguments to a JSON list written in a file.

"""
if __name__ == "__main__":

    import json
    from sys import argv
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__(
        '6-load_from_json_file').load_from_json_file

    json_list = load_from_json_file('add_item.json')
    json_list.append(argv[1:])
    save_to_json_file(json_list, 'add_item.json')
