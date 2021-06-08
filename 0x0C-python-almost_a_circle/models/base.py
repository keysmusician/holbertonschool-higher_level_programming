#!/usr/bin/python3
"""
Base class for project 0x0C. Python - Almost a circle.

"""


import json


class Base:
    """Define a base class to manage the 'id' attribute in derived classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize base class object."""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save 'list_objs' to a file in JSON format."""
        with open("{}.json".format(cls.__name__), 'w+') as file:
            dict_list = [obj.to_dictionary() for obj in list_objs]
            json_str = cls.to_json_string(dict_list)
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Deserialize and return a list of dictionaries in JSON format."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
