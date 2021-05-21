#!/usr/bin/python3
"""
Contains a function which divides a matrix.

>>> matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
>>> print(matrix_divided(matrix, 3))
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a number

    Return: a new matrix of the quotients of each element / div
    """
    # Validate input
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    size = None
    new_matrix = []
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(row)
        elif len(row) is not size:
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for n in row:
            if type(n) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_row.append(round(n / div, 2))
        new_matrix.append(new_row)

    return new_matrix
