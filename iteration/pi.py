#!/usr/bin/python3
from math import *

def square_root(a):
    x = 1.0
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < 0.00000001:
            return y
        x = y


def factorial(n):
    if n <= 1:
        return 1
    return factorial(n-1) * n


def estimate_pi():
    k = 0
    sum = 0

    while True:
        n = factorial(4*k) * (1103 + 26390*k)
        d = factorial(k)**4 * 396**(4*k)
        q = float(n) / d
        #print n, d, q
        if q < 10**-15:
            break
        sum = sum + q 
        k = k + 1

    return 9801 / (2 * square_root(2) * sum)

print (estimate_pi())
print (pi)
