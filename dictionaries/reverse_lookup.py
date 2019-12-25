#!/home/tgni/ml/env/bin/python3
from histogram import *

def reverse_lookup(d, v):
    r = []
    for k in d:
        if d[k] == v:
            r.append(k)
    return r

h = histogram('parrot')
for i in range(4):
    k = reverse_lookup(h, i)
    print k
