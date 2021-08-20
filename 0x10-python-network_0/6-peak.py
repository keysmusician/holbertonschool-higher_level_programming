#!/usr/bin/python3
"""A function which identifies peaks in a list of numbers."""


def find_peak(list_of_integers):
    """Find a peak in a list of integers."""
    try:
        peak = None
        prev_slope = 0
        for i, n in enumerate(list_of_integers):
            # print("index: {}; n: {}".format(i, n))

            # Skip first number, but save it as peak in case it's the only one
            if i == 0:
                peak = n
                continue

            # Calculate slope
            prev_n = list_of_integers[i - 1]
            slope = n - prev_n

            # If slope is positive or 0
            if slope >= 0:
                peak = n
            elif prev_slope > 0:
                return prev_n
            prev_slope = slope
        return peak
    except(TypeError):
        return None
