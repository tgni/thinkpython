#!/usr/bin/python3
def chop(t):
    del t[0]
    del t[-1]

t = ['a', 'b', 'c', 'd']
t1 = chop(t)
print t
print t1
