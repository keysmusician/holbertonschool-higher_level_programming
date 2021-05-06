#!/usr/bin/python3
def best_score(a_dictionary):
    """Return a key with the biggest integer value."""
    if a_dictionary:
        return max(zip(a_dictionary.values(), a_dictionary.keys()))[1]
