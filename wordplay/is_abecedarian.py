#!/home/tgni/ml/env/bin/python3
def is_abecedarian(word):
    length = len(word)

    if length <= 1:
        return True

    index = 1
    while index < length - 1:
        if ord(word[index-1]) > ord(word[index]):
            return False
        index += 1

    return True

fin = open('words.txt')
for line in fin:
    word = line.strip()
    if is_abecedarian(word):
        print word
