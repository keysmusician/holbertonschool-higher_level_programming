#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, n in enumerate(row):
            if i != 0:
                print(" {:d}".format(n), end="")
            else:
                print("{:d}".format(n), end="")
        print()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
