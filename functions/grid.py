#!/home/tgni/ml/env/bin/python3
def do_four(f, obj):
    f(obj)
    f(obj)
    f(obj)
    f(obj)

def p(s):
    """ for python2.7 format would be: 'print s,' """
    print(s, end=' ')

def print_plus_line():
    p('+')
    do_four(p, '-')
    p('+')
    do_four(p, '-')
    print('+')

def print_col_line(s):
    p(s)
    do_four(p, ' ')
    p(s)
    do_four(p, ' ')
    print(s)

def print_grid():
    print_plus_line()
    do_four(print_col_line, '|')
    print_plus_line()
    do_four(print_col_line, '|')
    print_plus_line()

print_grid()
