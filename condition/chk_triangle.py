#!/usr/bin/python3
def check_triangle(a, b, c):
    if a+b > c and a+c > b and b+c > a:
        print ('Yes')
    else:
        print ('No')
    

if __name__ == '__main__':
    a = input('a = ')
    b = input('b = ')
    c = input('c = ')
    check_triangle(int(a), int(b), int(c))
