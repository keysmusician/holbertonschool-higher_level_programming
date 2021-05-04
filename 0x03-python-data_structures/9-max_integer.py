#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list):
        maxint = my_list[0]
        for n in my_list:
            if n > maxint:
                maxint = n
        return maxint
