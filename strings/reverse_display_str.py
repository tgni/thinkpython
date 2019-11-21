def reverse_display(s):
    index = len(s) - 1
    while index >= 0:
        letter = s[index]
        print letter
        index = index - 1

s = raw_input('Pls input a string:')
reverse_display(s)
