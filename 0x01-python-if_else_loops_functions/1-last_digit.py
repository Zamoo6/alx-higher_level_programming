#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
m_rest = number % 10 if number > 10 else number % -10
print("Last digit of {:d} is {:d} and is ".format(number, m_rest), end="")
if m_rest > 5:
    print("greater than 5")
elif m_rest == 0:
    print("0")
else:
    print("less than 6 and not 0")
