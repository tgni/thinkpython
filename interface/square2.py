#!/usr/bin/python3

import turtle

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

bob = turtle.Turtle()
square(bob, 300)

turtle.mainloop()
