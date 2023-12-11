#!/usr/bin/python3
def is_palindrome(s):
    return s[::-1] == s

s = input('Pls input a string:')
print (is_palindrome(s))
