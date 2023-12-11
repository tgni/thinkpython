#!/usr/bin/python3

import turtle
from math import *

def polygon(t, length, n, angle):
    for i in range(int(n)):
        t.fd(length)
        t.rt(angle/n)

def circle(t, r):
    c      = 2 * pi * r
    length = 0.1
    n      = c / length
    polygon(t, length, n)

def arc(t, r, angle):
    l      = 2 * pi * r * angle / 360.0
    length = 3 
    n      = l / length
    polygon(t, length, n, angle)

bob   = turtle.Turtle()
#bob.delay = 0.000001
r = 100
arc(bob, r, 180)
bob.rt(90)
bob.fd(2 * r)

turtle.mainloop()
