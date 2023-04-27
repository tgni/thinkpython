#!/usr/bin/python3
def has_duplicates(t):
    for i in range(len(t)):
        for s in t[i+1:]:
            if t[i] == s:
                return True
    return False

t = ['a', 'e', 'c', 'd', 'e', 't', 's']
print (t, has_duplicates(t))
