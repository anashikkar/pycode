import math

def factorial(x):
    f = 1
    while x > 1:
        print x
        y = x
        sum = f * y
        x = x - 1
        f = sum
        print (y,sum)
    return sum
print factorial(6)
