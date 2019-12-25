#!/home/tgni/ml/env/bin/python3
def find(word, letter, pos):
    index = pos
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

s = raw_input('Pls input one string:')
i = raw_input('What position do you want to search?\r\n');
l = raw_input('Which letter do you want to search?\r\n')
j = find(s, l, int(i))
if j >= 0:
    print 'Yes!', 'get letter ', l, ' at ', j
else:
    print 'Oops!'
