#!/usr/bin/python3

import turtle

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.rt(360/n)

bob = turtle.Turtle()
polygon(bob, 80, 16)

turtle.mainloop()
