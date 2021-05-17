#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """Print x elements of a list, stopping safely if x > len(my_list)."""
    printed = 0
    for index in range(x):
        try:
            print(my_list[index], end="")
            printed += 1
        except IndexError:
            break
    print()
    return printed
