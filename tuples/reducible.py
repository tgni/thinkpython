from lists.inlist import *

def is_reducible(t, w):
    if len(word) <= 1:
        return True

    for i in range(len(word)-1):
        s = w[:i]+w[i+1:]
        if in_bisect(t, s):
            return is_reducible(t, s)
    return False

wordlist = make_word_list()
print wordlist
