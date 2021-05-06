!/usr/bin/python3
 def multiply_by_2(a_dictionary):
     """Return a new dictionary with all values multiplied by 2."""
    return dict([(key, val * 2) for key, val in a_dictionary.items()])
