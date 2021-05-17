#!/usr/bin/python3


def safe_print_division(a, b):
    """Divide two integers. Return None if undefined."""
    try:
        quotient = a / b
    except ZeroDivisionError:
        quotient = None
    finally:
        print("Inside result: {}".format(quotient))
    return quotient
