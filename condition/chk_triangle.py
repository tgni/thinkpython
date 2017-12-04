def check_triangle(a, b, c):
    if a+b > c and a+c > b and b+c > a:
        print 'Yes'
    else:
        print 'No'
    

if __name__ == '__main__':
    a = raw_input('a = ')
    b = raw_input('b = ')
    c = raw_input('c = ')
    check_triangle(int(a), int(b), int(c))
