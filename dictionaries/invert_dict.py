#!/usr/bin/python3

from histogram import *

def invert_dict(d):
    inverse = dict()
    for key, val in d.iteritems():
        inverse.setdefault(val, []).append(key)
    return inverse


hist = histogram('parrot') 
print hist
print invert_dict(hist)
