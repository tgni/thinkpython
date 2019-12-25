#!/usr/bin/python3
from random import *

def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), word))
        t.sort(reverse=True)
    res = []
    for length, word in t:
        res.append(word)
    return res

def sort_by_length_random(words):
    t = []
    for word in words:
        t.append((len(word), 100*random(), word))
        t.sort(reverse=True)
    res = []
    for length, rand, word in t:
        res.append(word)
    return res

if __name__ == '__main__':
    t = ['abc', 'aa', 'cc', 'deb', 'adfwe', 'fewe', 'dafef', 'adsfwefad', 'dfefe']
    s  = sort_by_length(t)
    s1 = sort_by_length_random(t)
    print t
    print s
    print s1
