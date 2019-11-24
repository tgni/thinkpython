#!/usr/bin/python
def do_four_obj(f, obj):
    f(obj)
    f(obj)
    f(obj)
    f(obj)

def do_four(f):
    f()
    f()
    f()
    f()

def p(s):
    print s,

def print_plus():
    p('+')
    do_four_obj(p, '-')

def print_plus_line():
    do_four(print_plus)
    print '+'

def print_col():
    p('|')
    do_four_obj(p, ' ')

def print_col_line():
    do_four(print_col)
    print '|'

def print_one_grid():
    print_plus_line()
    do_four(print_col_line)

def print_grid():
    do_four(print_one_grid)
    print_plus_line()

print_grid()
