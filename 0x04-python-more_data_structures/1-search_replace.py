#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """In a new list, replace all occurrences of an element with another."""
    return list(map(lambda item: replace if item == search else item, my_list))
