#!/usr/bin/python3

import copy

from point2 import Point
from rectangle import Rectangle

class Circle:
    """ center, radius """
    def __init__(self, center = Point(), radius = 1):
        self.center = center
        self.radius = radius

    def __str__(self):
        if isinstance(self.center, Point):
            return 'center: (%g, %g) radius: %g' % (self.center.x, self.center.y, self.radius)
        else:
            return 'center: (%g, %g) radius: %g' % (self.center[0], self.center[1], self.radius)

def point_in_circle(point, circle):
    if (point.x - circle.center.x) ** 2 + (point.y - circle.center.y) ** 2 <= circle.radius ** 2:
        return True
    else:
        return False

def rect_in_circle(rect, circle):
    p = copy.copy(rect.corner)
    if not point_in_circle(p, circle):
        return False
    p.x += rect.width
    if not point_in_circle(p, circle):
        return False
    p.y -= rect.height
    if not point_in_circle(p, circle):
        return False
    p.x -= rect.width
    if not point_in_circle(p, circle):
        return False
    return True

if __name__ == '__main__':
    #cir = Circle((150, 100), 75)
    cir = Circle(Point(150, 100), 75)
    print(cir)

    p = Point(150, 100)
    print(p, point_in_circle(p, cir))
    p = Point(150, 120)
    print(p, point_in_circle(p, cir))
    p = Point(150, 170)
    print(p, point_in_circle(p, cir))
    p = Point(150, 175)
    print(p, point_in_circle(p, cir))
    p = Point(150, 200)
    print(p, point_in_circle(p, cir))

    p = Point(150, 100)
    print(p, point_in_circle(p, cir))
    p = Point(160, 100)
    print(p, point_in_circle(p, cir))
    p = Point(220, 100)
    print(p, point_in_circle(p, cir))
    p = Point(225, 100)
    print(p, point_in_circle(p, cir))
    p = Point(230, 100)
    print(p, point_in_circle(p, cir))
