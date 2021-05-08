#!/usr/bin/python3
def weight_average(my_list=[]):
    """Return the weighted average of a list of 2-integer tuples."""
    wgt_count = sum([y for x, y in my_list])
    return sum([x * y for x, y in my_list]) / wgt_count if wgt_count else 0
