#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Return the square value of all integers of a matrix as a new matrix."""
    return [list(map(lambda x : x**2, row)) for row in matrix]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
