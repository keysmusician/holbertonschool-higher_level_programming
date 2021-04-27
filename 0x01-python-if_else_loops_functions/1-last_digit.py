#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
signedLastDigit = abs(number) % 10 * (number // abs(number))
print("Last digit of {} is {} and is".format(number, signedLastDigit), end=' ')
if signedLastDigit == 0:
    print("0")
elif signedLastDigit > 5:
    print("greater than 5")
elif signedLastDigit < 6:
    print("less than 6 and not 0")
