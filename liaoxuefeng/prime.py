#!/usr/bin/python3
# -*- coding: utf-8 -*-

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # ��ʼ����
    while True:
        n = next(it) # �������еĵ�һ����
        yield n
        it = filter(_not_divisible(n), it) # ����������

# ��ӡ1000���ڵ�����:
for n in primes():
    if n < 1000:
        print(n, end=' ')
    else:
        print(' ')
        break
