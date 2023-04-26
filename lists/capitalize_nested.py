#!/usr/bin/python3
"""
begin a word with capital letter
"""
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

def capitalize_nested(t):
    res = []
    for s in t:
        if isinstance(s, list):
            res.append(capitalize_all(s))
        else:
            res.append(s.capitalize())
    return res

t = ['hi,', 'i', 'am', ['ni', 'tonggui']]
T = capitalize_nested(t)
print t
print T
