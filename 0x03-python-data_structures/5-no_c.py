#!/usr/bin/python3
def no_c(my_string):
    new_string = "".join([x for x in my_string if x not in "Cc"])
    return new_string
