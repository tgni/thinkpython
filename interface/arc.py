#!/usr/bin/python3

#from swampy.TurtleWorld import *
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
    length = 5 
    n      = l / length
    polygon(t, length, n, angle)

#world = TurtleWorld()
bob   = turtle.Turtle()
#bob.delay = 0.000001

arc(bob, 250, 180)
bob.rt(90)
bob.fd(2 * 250)

turtle.mainloop()
