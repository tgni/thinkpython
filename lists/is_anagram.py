def is_anagram(s, t):
    if s[::-1] == t:
        return True
    return False

s = 'abcdef'
t = 'fedcba'
print s, t, is_anagram(s, t)
