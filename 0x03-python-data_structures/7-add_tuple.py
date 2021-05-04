#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = (
        tuple_a[0:1] + tuple_b[0:1],
        tuple_a[1:2] + tuple_b[1:2]
    )
    sums = [sum(pair) for pair in tuple_c]
    return tuple(sums)
