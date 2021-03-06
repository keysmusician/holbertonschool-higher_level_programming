#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    n_args = len(argv) - 1
    if n_args > 0:
        s = "s" if n_args > 1 else ""
        print("{} argument{}:".format(n_args, s))
        for i, arg in enumerate(argv[1:], 1):
            print("{}: {}".format(i, arg))
    else:
        print("0 arguments.")
