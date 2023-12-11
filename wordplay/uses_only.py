#!/usr/bin/python3
def uses_only(word, string):
    for x in word:
        if string.find(x) < 0:
            return False
    return True
            
pattern = input('Pls input letters pattern:')
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if uses_only(word, pattern):
        print word
