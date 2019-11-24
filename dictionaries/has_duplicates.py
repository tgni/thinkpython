#!/usr/bin/python
def has_duplicates(t):
    d = {}

    for x in t:
        if x in d:
            return True
        d[x] = True

def has_duplicates2(t):
    return len(set(t)) < len(t)

t = ['a', 'e', 'c', 'd', 'e', 't', 's']
print t, has_duplicates(t)
