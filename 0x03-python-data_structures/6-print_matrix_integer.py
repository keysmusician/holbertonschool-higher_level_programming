#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, n in enumerate(row):
            if i != 0:
                print(" {:d}".format(n), end="")
            else:
                print("{:d}".format(n), end="")
        print('')
