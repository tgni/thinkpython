#!/home/tgni/ml/env/bin/python3
from lists.inlist import *

def list_find(t, w):
    for x in t:
        if x == w:
            return True
    return False

def get_children(wordlist, word):
    se = []
    se.append([word])
    i = 0
    while True:
        wt = se[i]
        ju = []
        for w in wt:
            for j in range(len(w)):
                s = w[:j]+w[j+1:]
                #if not list_find(ju, s) and (in_bisect(wordlist, s) or len(s) == 1):
                if not list_find(ju, s):
                    if in_bisect(wordlist, s):
                        ju.append(s)
                    elif len(s) == 1 and (s == 'i' or s == 'a'):
                        ju.append(s)
        if len(ju) > 0:
            se.append(ju)
            i += 1
        else:
            break
    return se
          
wordlist = make_word_list()
for word in wordlist:
    se = get_children(wordlist, word)
    if len(se) == len(word):
        print word, se
