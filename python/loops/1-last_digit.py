#!/usr/bin/env python3
import random
number = random.randint(-10000, 10000)
# generate a number between -999 and +999
x = number % 10
if x > 5:
    print("Last digit of", number, "is", x, "and is greater than 5")
elif x < 6:
    print("Last digit of", number, "is", x, "and is less than 6 and not zero")
else:
    print("Last digit of ", number, "is", x, "and is zero")
