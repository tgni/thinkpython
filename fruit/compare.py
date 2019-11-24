#!/usr/bin/python
def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1;

if __name__ == '__main__':
    x = raw_input('x = ')
    y = raw_input('y = ')
    r = compare(int(x), int(y))
    print 'x = ' + x + ', y = ' + y + ', r = ' + str(r)
