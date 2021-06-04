#!/usr/bin/python3
"""A function that returns a representation of Pascal’s triangle."""


def pascal_triangle(n):
    """
    Return a list of lists of integers representing the Pascal’s triangle of n.

    """
    result = []
    if n > 0:
        result.append([1])
        for r in range(n - 1):
            last_row = result[r]
            next_row = [
                sum(pair) for pair in zip([0] + last_row, last_row + [0])
            ]
            result.append(next_row)
    return result
