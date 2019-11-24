#!/usr/bin/python
def remove_duplicates(t):
    res = []
    for e in t:
        for s in res:
            if e == s:
                break 
        else:
            res.append(e)
    return res

t = ['a', 'e', 'e', 'f', 's', 't', 's']
print t
s = remove_duplicates(t)
print s
