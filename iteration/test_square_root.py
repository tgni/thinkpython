#!/usr/bin/python
from math import *

def square_root(a):
    x = 1
    while True:
        y = (x + a/x) / 2
        if abs(y-x) < 0.00000001:
            return y
        x = y

def test_square_root():
    i = 1.0
    while i < 10:
        p = square_root(i)
        q = sqrt(i)
        #print '%-3f %-.11f %-.11f %e' % (i, p, q, q - p)
        print '%-3s %-13s %-13s %-17s' % (str(i), str(p), str(q), str(q - p))
        i = i + 1

test_square_root()
