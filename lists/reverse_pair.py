#!/usr/bin/python
from inlist import *

def reverse_pair(t, word):
    return in_bisect(t, word[::-1])

if __name__  == '__main__':
    word_list = make_word_list()
    for word in word_list:
        if reverse_pair(word_list, word):
            print word, word[::-1]
