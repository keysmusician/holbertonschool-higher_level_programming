#!/usr/bin/python3
"""
A function that formats text.

"""


def text_indentation(text):
    """Prints text with 2 new lines after any '.', ':' or '?'."""
    if type(text) is not str:
        raise TypeError("text must be a string")

    start = 0
    for i, c in enumerate(text):
        if c in ".:?":
            print(text[start:i + 1].lstrip() + "\n")
            start = i + 1
    print(text[start:].strip(), end='')
