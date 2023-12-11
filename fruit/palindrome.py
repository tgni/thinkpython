#!/usr/bin/python3
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1] #not include -1

s = 'hello world'
#s = ''
#s = 'he'
#s = 'h'

print ("s:" + s)
print ("first:" + first(s))
print ("last:" + last(s))
print ("middle:" + middle(s))
