#!/usr/bin/python3
def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1;

if __name__ == '__main__':
    x = input('x = ')
    y = input('y = ')
    r = compare(int(x), int(y))
    print ('x = ' + x + ', y = ' + y + ', r = ' + str(r))
