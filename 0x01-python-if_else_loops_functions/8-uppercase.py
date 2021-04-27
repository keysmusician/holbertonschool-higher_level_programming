#!/usr/bin/python3
def uppercase(str):
    for c in str:
        print("{:c}".format(ord(c) - 32), end='')
    print()
