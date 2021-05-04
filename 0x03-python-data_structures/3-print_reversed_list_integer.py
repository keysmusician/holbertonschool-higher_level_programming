#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for n in reversed(my_list):
        print("{:d}".format(n))
    if len(my_list) is 0:
        print('')
