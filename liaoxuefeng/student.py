#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
double `__' defined private variables in python
'''

class Student(object):
    
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpon', 59)
lisa = Student('Lisa Simpon', 87)

#print('bart.name=', bart.__name)
#print('bart.score=', bart.__score)
print('bart.name=', bart._Student__name)
print('bart.score=', bart._Student__score)
bart.print_score()

print('grade of Bart:', bart.get_grade())
print('grade of Lisa:', lisa.get_grade())
