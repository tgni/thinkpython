#!/usr/bin/python3
def has_no_e(word):
    if word.find('e') < 0:
        return True
    return False 

s = input('Pls input a string:')
print has_no_e(s)
