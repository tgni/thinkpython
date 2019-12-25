#!/usr/bin/python3
from swampy.TurtleWorld import *


def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)


world = TurtleWorld()
bob = Turtle()

pu(bob)
lt(bob, 180)
fd(bob, 200)
lt(bob, 90)
fd(bob, 200)
lt(bob, 90)
pd(bob)
draw(bob, 20, 5)

wait_for_user()
