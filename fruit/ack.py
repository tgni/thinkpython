#!/usr/bin/python3

def ack(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ack(m - 1, 1)
    if m > 0 and n > 0:
        return ack(m - 1, ack(m, n -1))

r = ack(3, 4)
print (r)
