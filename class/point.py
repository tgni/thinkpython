#!/usr/bin/python3

import math

class Point:
    """ x, y 2-D space. """
    def __init__ (self, x = 0, y = 0):
        self.x = x
        self.y = y

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

def distance_between_points(a, b):
    return math.sqrt((a.x - b.x) ** 2 +  (a.y - b.y) ** 2)

if __name__ == '__main__':
    a = Point()
    a.x = 1
    a.y = 1
    b = Point()
    b.x = 2
    b.y = 2
    print('a', end=':')
    print_point(a)
    print('b', end=':')
    print_point(b)
    print("distance: ", distance_between_points(a, b))
