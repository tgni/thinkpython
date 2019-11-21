def check_fermat(a, b, c, n):
    if a**n + b**n  == c**n:
        print 'Holy smokes, Fermat was wrong!'
    else:
        print 'No, that doesn\'t work.'

if __name__ == '__main__':
    a = raw_input('a = ')
    b = raw_input('b = ')
    c = raw_input('c = ')
    n = raw_input('n = ')
    check_fermat(int(a), int(b), int(c), int(n))
