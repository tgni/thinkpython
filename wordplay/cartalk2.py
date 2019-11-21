def is_palindrome(s, start, end):
    s = 
    return s[::-1] == s

n = 100000
max = 999999

while n < max:
    if is_palindrome(str(n)):
        print n
    n = n+1

