#!/usr/bin/python3
def best_score(a_dictionary):
    """Return a key with the biggest integer value."""
    return a_dictionary[max(a_dictionary)] if a_dictionary else None
