#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":

    if len(argv[1:]) is not 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])

    if len(op) > 1 or op not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if op == '+':
        result = add(a, b)
    elif op == '-':
        result = sub(a, b)
    elif op == '*':
        result = mul(a, b)
    elif op == '/':
        result = div(a, b)

    print("{} {} {} = {}".format(a, op, b, result))
    exit(0)
