#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """Divide elements at equal indecies of two lists."""
    result = []
    for index in range(list_length):
        quotient = 0
        try:
            quotient = my_list_1[index] / my_list_2[index]
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        finally:
            result.append(quotient)
    return result
