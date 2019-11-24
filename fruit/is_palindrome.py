#!/usr/bin/python
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if (first(s) != last(s)):
        return False
    return is_palindrome(middle(s))


s0 = 'redivider'
s1 = 'hello'
s2 = 'ollo'

print s0 + "is " + str(is_palindrome(s0))
print s1 + "is " + str(is_palindrome(s1))
print s2 + "is " + str(is_palindrome(s2))

