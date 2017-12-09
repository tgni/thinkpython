"""
def make_key(word):
    d = {}
    t = []
    for x in word:
        d[x] = d.get(x, 0) + 1
    for x in d:
        t.append((x, d[x]))
    return tuple(t)
"""
from unstable_sort import *

def make_key(word):
    t = list(word)
    t.sort()
    return ''.join(t)

if __name__ == '__main__':
    fin = open('../wordplay/words.txt')
    ana = {}
    for line in fin:
        word = line.strip()
        key = make_key(word)
        ana.setdefault(key, []).append(word)
    
    t = []
    for k in ana:
        if len(ana[k]) > 1:
            t += ana[k]
    t1 = sort_by_length(t)
    for e in t1:
        print e
