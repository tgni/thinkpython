#!/usr/bin/python
from swampy.TurtleWorld import *
from math import *

def polygon(t, length, n):
    for i in range(int(n)):
        fd(t, length)
        rt(t, 360/n)


def circle(t, r):
    c      = 2 * pi * r
    length = 0.1
    n      = c / length;
    polygon(t, length, n)

world = TurtleWorld()
bob   = Turtle()
bob.delay = 0.000001

circle(bob, 100)

wait_for_user()
