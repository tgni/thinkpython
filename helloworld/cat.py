#!/usr/bin/python
def print_twice(str):
    print str
    print str

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

line1 = 'Bing tiddle '
line2 = 'tiddle bang.'

cat_twice(line1, line2)
