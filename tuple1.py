# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 14:10:48 2021

@author: 경진
"""

### 튜플
score = (88, 95, 70, 100, 99)


### onetuple
tu = 2,
value = 2
print(tu)


### tupleop
tu = 1, 2, 3, 4, 5
print(tu[3])
print(tu[1:4])
print(tu + (6, 7))
print(tu * 2)


### unpacking
tu = "이순신", "김유신", "강감찬"
lee, kim, kang = tu
print(lee)
print(kim)
print(kang)


## swap
a, b = 12, 34
print(a, b)
a, b = b, a
print(a, b)