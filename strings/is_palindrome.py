#!/usr/bin/python
def is_palindrome(s):
    return s[::-1] == s

s = raw_input('Pls input a string:')
print is_palindrome(s)
