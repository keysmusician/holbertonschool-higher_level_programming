#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10
print("Last digit of {} is {} and is".format(number, lastDigit), end = ' ')
if lastDigit == 0:
    print("0")
elif lastDigit > 5:
    print("greater than 5")
elif lastDigit < 6:
    print("less than 6 and not 0")
