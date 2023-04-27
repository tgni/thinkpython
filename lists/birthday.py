#!/usr/bin/python3
from random import *

def has_duplicates(t, dup):
    for i in range(len(t)):
        for s in t[i+1:]:
            if t[i] == s:
                dup[0] = t[i] 
                return True
    return False

def random_birthday():
    return randint(1, 365)

p = 0
for j in range(1000):
    t = []
    for i in range(23):
        t.append(random_birthday())
    dup = [0]
    if has_duplicates(t, dup):
        p += 1
        print(t, dup)
print ('chance:', p * 100.0 / 1000, '%')
