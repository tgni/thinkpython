#!/usr/bin/python3
def check_fermat(a, b, c, n):
    if a**n + b**n  == c**n:
        print ('Holy smokes, Fermat was wrong!')
    else:
        print ('No, that doesn\'t work.')

if __name__ == '__main__':
    a = input('a = ')
    b = input('b = ')
    c = input('c = ')
    n = input('n = ')
    check_fermat(int(a), int(b), int(c), int(n))
