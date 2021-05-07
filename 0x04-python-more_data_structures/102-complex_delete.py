#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if type(a_dictionary) is dict:
        del_keys = [key for key, val in a_dictionary.items() if val == value]
        for key in del_keys:
            a_dictionary.pop(key)
    return a_dictionary
