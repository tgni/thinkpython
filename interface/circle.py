#!/usr/bin/python3

import turtle
import math

# n refer as n-sided regular polygon
# length refer as side length
def polygon(t, length, n):
    for i in range(int(n)):
        t.fd(length)
        t.rt(360/n)


def circle(t, r):
    c      = 2 * math.pi * r
    length = 3
    n      = c / length;
    polygon(t, length, n)

bob = turtle.Turtle()
#bob.delay = 0.01

circle(bob, 100)

turtle.mainloop()
