#!/usr/bin/python
def avoids(word, forbid):
    for x in word:
        for y in forbid:
            if x == y:
                return False
    return True

forbid = raw_input('Pls input forbidden letters pattern:')
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if avoids(word, forbid):
        print word


