#!/usr/bin/python3
"""
assume list can be compared with relational operators <,> etc.
"""

def is_sorted(t):
    for i in range(len(t)-1):
        if t[i] > t[i+1]:
            return False
    return True

t = ['a', 'c', 'e', 'h', 'i', 'd']
print (t)
print (is_sorted(t))
t.sort()
print (t)
print (is_sorted(t))
