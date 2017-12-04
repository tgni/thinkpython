from swampy.TurtleWorld import *
from math import *

def polygon(t, length, n, angle):
    for i in range(int(n)):
        fd(t, length)
        rt(t, angle/n)

def circle(t, r):
    c      = 2 * pi * r
    length = 0.1
    n      = c / length
    polygon(t, length, n)

def arc(t, r, angle):
    l = 2 * pi * r * angle / 360.0
    length = 0.1
    n = l / length
    polygon(t, length, n, angle)

world = TurtleWorld()
bob   = Turtle()
bob.delay = 0.000001

arc(bob, 100, 180)

bob.delay = 1
rt(bob, 90)
fd(bob, 2 * 100)

wait_for_user()
