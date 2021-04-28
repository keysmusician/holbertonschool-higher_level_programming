#!/usr/bin/python3
def magic_calculation(a, b, c):
    if not a < b:
        return c
    if not c > b:
        return a + b
    return a * b - c
