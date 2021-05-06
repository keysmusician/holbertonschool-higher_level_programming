#!/usr/bin/python3
def roman_to_int(roman_string):
    """Convert a Roman numeral to an integer."""
    conversion = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    if type(roman_string) is not str:
        return 0
    return sum([-conversion[N] if conversion.get(roman_string[i + 1: i + 2],
                0) > conversion[N] else conversion[N]
                for i, N in enumerate(roman_string)])
