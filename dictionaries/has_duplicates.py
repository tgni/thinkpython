#!/usr/bin/python3
def has_duplicates(t):
    d = {}
    for x in t:
        if x in d:
            return True
        d[x] = True

def has_duplicates2(t):
    return len(set(t)) < len(t)

t = ['a', 'e', 'c', 'd', 'e', 't', 's']
print(t, set(t))
print (t, has_duplicates(t), has_duplicates2(t))
