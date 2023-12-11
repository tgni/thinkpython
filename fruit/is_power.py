#!/usr/bin/python3
def is_power(a, b):
    if a == b:
        return True
    if b <= 0 or a < b:
        return False
    return is_power(a/b, b)

print (is_power(1000, 10))
print (is_power(1024, 2))
print (is_power(1023, 2))
