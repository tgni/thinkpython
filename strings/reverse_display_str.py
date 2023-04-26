#!/usr/bin/python3
def reverse_display(s):
    index = len(s) - 1
    rs = ""
    while index >= 0:
        letter = s[index]
        rs += letter
        index = index - 1
    return rs

s = input('Pls input a string:')
rs = reverse_display(s)
print(rs)
