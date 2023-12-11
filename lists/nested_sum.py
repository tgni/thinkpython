#!/usr/bin/python3
#import types
def nested_sum(t):
    total = 0
    for i in t:
        #if type(i) is types.ListType:
        if isinstance(i, list):
            total += nested_sum(i)
        else:
            total += i
    return total

t = [1, 2, 3, [4, 5], [6, 7, [1, 1, [1, 1],1], 8]]
print (nested_sum(t))
