#!/usr/bin/python3
def print_twice(obj):
    print obj
    print obj

def do_twice(f, obj):
    f(obj)
    f(obj)

do_twice(print_twice, 'spam')
