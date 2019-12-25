#!/home/tgni/ml/env/bin/python3
import string

fin = open('tmp.txt')
wordlist = []
for line in fin:
    line = line.strip()
    wordlist += line.split(' ')
    #word = line.translate(None, string.whitespace)
    #word = word.translate(None, string.punctuation)
    #words = words.lower()
print wordlist
