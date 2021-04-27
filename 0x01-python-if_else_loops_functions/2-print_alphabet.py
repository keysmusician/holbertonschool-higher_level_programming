#!/usr/bin/python3
ASCII_a, ASCII_z = 97, 122
for c in range(ASCII_a, ASCII_z + 1):
    print("{:c}".format(c), end='')
