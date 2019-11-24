#!/usr/bin/python
def sum_list(t):
    res = []
    sum = 0
    for s in t:
        sum += s
        res.append(sum)
    return res

t = [1, 2, 3, 4, 5, 6, 7, 8, 9]
t1 = sum_list(t)

print t
print t1
