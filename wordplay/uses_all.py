#!/usr/bin/python3
def uses_all(word, string):
    for x in string:
        if word.find(x) < 0:
            return False
    return True
            
pattern = input('Pls input letters pattern:')
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if uses_all(word, pattern):
        print word
