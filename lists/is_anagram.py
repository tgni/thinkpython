#!/usr/bin/python3
def is_anagram(s, t):
    print(s[::-1], t)
    if s[::-1] == t:
        return True
    return False

s = 'abcdef'
t = 'fedcba'
print (s, t, is_anagram(s, t))
