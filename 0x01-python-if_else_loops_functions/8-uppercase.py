#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if c in range(ord('a'), ord('z') + 1):
            print("{:c}".format(ord(c) - 32), end='')
    print()
