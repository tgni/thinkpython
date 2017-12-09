from unstable_sort import *

def is_metathesis(a, b):
    time = 0
    diff = []
    for i in range(len(a)):
        if a[i] != b[i]:
            diff.append((a[i], b[i]))
            if (len(diff) > 2):
                return False
    return True

def find_metathesis(t):
    for i in range(len(t)-1):
        for x in t[i+1:]:
            if is_metathesis(t[i], x):
                return t[i], x
    return None

def make_key(word):
    t = list(word)
    t.sort()
    return ''.join(t)

if __name__ == '__main__':
    fin = open('../wordplay/words.txt')
    ana = {}
    for line in fin:
        word = line.strip()
        key = make_key(word)
        ana.setdefault(key, []).append(word)
    
    for t in ana.itervalues():
        if len(t) > 1:
            e = find_metathesis(t)
            if e:
                print e
