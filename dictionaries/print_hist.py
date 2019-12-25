#!/home/tgni/ml/env/bin/python3
from histogram import *
"""
def print_hist(h):
    for c in h:
        print c, h[c]
"""

def print_hist(h):
    k = h.keys()
    k.sort()
    for c in k:
        print c, h[c]

h = histogram('parrot')
print_hist(h)
