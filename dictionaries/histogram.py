#!/usr/bin/python3
def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1 # d.get(c, 0): returns value otherwise 0.
    return d
"""
h = histogram('brontosaurus')
print (h)
print (h.items())
"""
