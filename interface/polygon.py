#!/usr/bin/python
from swampy.TurtleWorld import *

def polygon(t, length, n):
    for i in range(n):
        fd(t, length)
        rt(t, 360/n)

world = TurtleWorld()
bob   = Turtle()
polygon(bob, 50, 8)

wait_for_user()
