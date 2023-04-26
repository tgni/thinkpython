#!/usr/bin/python3
def print_twice(obj):
    print obj
    print obj

def do_twice(f, obj):
    f(obj)
    f(obj)

def do_four(f, obj):
    do_twice(f, obj)

do_four(print_twice, 'spam')
