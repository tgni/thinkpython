#!/usr/bin/python
from random import *

def has_duplicates(t):
    for i in range(len(t)):
        for s in t[i+1:]:
            if t[i] == s:
                return True
    return False

def random_birthday():
    return randint(1, 365)

p = 0
for j in range(1000):
    t = []
    for i in range(23):
        t.append(random_birthday())
    if has_duplicates(t):
        p += 1
print 'chance:', p * 100.0 / 1000, '%'
