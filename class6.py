# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 17:44:37 2021

@author: 경진
@comment: 유틸리티 클래스 
"""


### Decimal : 정확하게 10진 실수 표현
from decimal import Decimal

f = 0.1
sum = 0
for i in range(100):
    sum += f
print(sum)      # float error


f = Decimal('0.1')
sum = 0
for i in range(100):
    sum += f
print(sum)


### Fraction : 분수 표현
from fractions import Fraction
a = Fraction(1, 3)
print(a)
b = Fraction(8, 14)
print(b)