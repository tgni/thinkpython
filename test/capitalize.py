#!/usr/bin/python3

def capitalize_all(t):
    r = []
    for s in t:
        r.append(s.capitalize())
        #r.append(s.upper())
    return r

t = ['aaaa', 'bbbb', 'cccc']
print(t)
new_t = capitalize_all(t)
print(new_t)
