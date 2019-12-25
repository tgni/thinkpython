#!/home/tgni/ml/env/bin/python3
fin = open('words.txt')

wordsDic = dict() 
for line in fin:
    word = line.strip()
    wordsDic[word] = 1

print wordsDic

