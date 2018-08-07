import random
import math

print("Think of number between 1 and 10")


def guess():
    a = int(input("Think of a number between 1 and: "))
    a1 = 1
    a2 = 10
    b = 4
    c = (input("Is it lower than " + math.floor(a2/2)))
    if c == 'yes':
        a2 = math.floor(a2/2)
    elif c == 'no':
        a1 = math.floor(a2/2)
