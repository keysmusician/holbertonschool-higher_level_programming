#!/usr/bin/python3
def weight_average(my_list=[]):
    """Return the weighted average of a list of 2-integer tuples."""
    return sum([x * y for x, y in my_list]) / sum([y for x, y in my_list])
