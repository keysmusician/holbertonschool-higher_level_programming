#!/usr/bin/python3
def roman_to_int(roman_string):
    """Convert a Roman numeral to an integer."""
    if type(roman_string) is not str:
        return 0
    arabic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ints = [arabic[N] for N in roman_string]
    return sum(map((lambda x, y: -x if x < y else x), ints, ints[1:] + [0]))
