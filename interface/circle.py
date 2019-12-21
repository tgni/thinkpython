#!/usr/bin/python3

import turtle
import math

def polygon(t, length, n):
    for i in range(int(n)):
        t.fd(length)
        t.rt(360/n)


def circle(t, r):
    c      = 2 * math.pi * r
    length = 1
    n      = c / length;
    polygon(t, length, n)

bob = turtle.Turtle()
#bob.delay = 0.01

circle(bob, 100)

turtle.mainloop()
