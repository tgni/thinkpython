#!/usr/bin/python3

from point import Point, print_point
import copy

class Rectangle:
    """ Represents a rectangle
    attributes: width, height, corner
    """
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
    print_point(center)
    print("box orig:", box.width, box.height, 'corner', end=':')
    print_point(box.corner)
    grow_rectangle(box, 100, 200)
    move_rectangle(box, 10, 20)
    print("box now:", box.width, box.height, 'corner', end=':')
    print_point(box.corner)

    new = move_rectangle2(box, 10, 20)
    print("after move rectangle2:")
    print("box now:", box.width, box.height, 'corner', end=':')
    print_point(box.corner)
    print("new now:", new.width, new.height, 'corner', end=':')
    print_point(new.corner)

    box2 = copy.copy(box)
    print(box2 is box)
    print(box2.corner is box.corner)

    box3 = copy.deepcopy(box)
    print(box3 is box)
    print(box3.corner is box.corner)

