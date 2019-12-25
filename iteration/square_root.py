#!/usr/bin/python3
from math import *

def square_root(a, x):
    while True:
        print x
        y = (x + a/x) / 2
        if abs(y-x) < 0.00000001:
            return y
        x = y

a = float(raw_input('Pls input a number:'))
x = float(raw_input('Pls input a x for iteration:'))

print 'Square of ' + str(a) + 'is ' + str(square_root(a, x))
