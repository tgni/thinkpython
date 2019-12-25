#!/home/tgni/ml/env/bin/python3
def has_no_e(word):
    if word.find('e') < 0:
        return True
    return False 

fin = open('words.txt')
total = 0
noe   = 0
for line in fin:
    total += 1
    word = line.strip()
    if has_no_e(word):
        noe +=1

print noe, total, noe * 1.0 / total

