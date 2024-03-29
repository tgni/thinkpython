#!/usr/bin/python3

import turtle

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

bob = turtle.Turtle()

bob.pu() #pen up
bob.lt(180)
bob.fd(200)
bob.lt(90)
bob.fd(200)
bob.lt(90)
bob.pd() #pen down
draw(bob, 20, 5)

turtle.mainloop()
