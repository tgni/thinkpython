#!/usr/bin/python3

from point2 import Point
import copy

class Rectangle:
    """ Represents a rectangle
    attributes: width, height, corner
    """
    def __init__(self, corner = Point(), width = 0, height = 0):
        self.corner = corner
        self.width = width
        self.height = height
    def __str__(self):
        return "corner: (%g %g) width: %g height: %g" % (self.corner.x, self.corner.y, self.width, self.height)

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight

def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy

def move_rectangle2(rect, dx, dy):
    new = copy.deepcopy(rect)
    new.corner.x += dx
    new.corner.y += dy
    return new

if __name__ == '__main__':
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0
    center = find_center(box)
    print(center)
    print("box orig:", box.width, box.height, 'corner', end=':')
    print(box.corner)
    grow_rectangle(box, 100, 200)
    move_rectangle(box, 10, 20)
    print("box now:", box.width, box.height, 'corner', end=':')
    print(box.corner)

    new = move_rectangle2(box, 10, 20)
    print("after move rectangle2:")
    print("box now:", box.width, box.height, 'corner', end=':')
    print(box.corner)
    print("new now:", new.width, new.height, 'corner', end=':')
    print(new.corner)

    box2 = copy.copy(box)
    print(box2 is box)
    print(box2.corner is box.corner)

    box3 = copy.deepcopy(box)
    print(box3 is box)
    print(box3.corner is box.corner)

