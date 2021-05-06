#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Return a new matrix with the square of all integers of a matrix."""
    return [list(map(lambda x: x**2, row)) for row in matrix]
