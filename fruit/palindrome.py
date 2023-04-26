#!/usr/bin/python3
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

s = 'hello world'
#s = ''
#s = 'he'
#s = 'h'

print s
print first(s)
print last(s)
print middle(s)
