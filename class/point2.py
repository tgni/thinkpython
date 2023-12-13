#!/usr/bin/python3

import math

class Point:
    """ x, y 2-D space. """
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

    def add_point(self, other):
        new = Point()
        new.x = self.x + other.x
        new.y = self.x + other.y
        return new

    def increment(self, other):
        new = Point()
        new.x = self.x + other[0] 
        new.y = self.x + other[1]
        return new

    def __add__(self, other):
        if isinstance(other, Point):
            print("type(other):", type(other))
            return self.add_point(other)
        else:
            print("type(other):", type(other))
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)

def distance_between_points(a, b):
    return math.sqrt((a.x - b.x) ** 2 +  (a.y - b.y) ** 2)

def print_attr(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))

if __name__ == '__main__':
    a = Point(1, 1)
    b = Point(2, 2)
    print(a, b, "distance: %.3f " % distance_between_points(a, b))
    print(a, b, a+b)
    c = a + b
    print('a+b:', c)
    c = a + (2, 2)
    print('a+(2,2):', c)
    c = (2, 2) + a
    print('(2,2)+a:', c)
    print_attr(c)
