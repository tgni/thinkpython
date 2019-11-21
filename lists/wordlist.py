from time import *

fin = open('words.txt')

t = []
t1 = time()
for line in fin:
    t.append(line)
t1 = time() - t1

t = []
t2 = time()
for line in fin:
    t = t + [line]
t2 = time() - t2

print t1, t2
