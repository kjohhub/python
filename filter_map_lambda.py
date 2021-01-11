# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 16:47:13 2021

@author: 경진
"""

score = [45, 89, 72, 53, 94]
bonus = [2, 3, 0, 0, 5]


### filter
def flunk(s):
    return s < 60

for s in filter(flunk, score):
    print(s, end = ', ')
print()
    
    
### map
def half(s):
    return s/2

for s in map(half, score):
    print(s, end= ', ')
print() 

    
### map2
def total(s, b):
    return s + b

for s in map(total, score, bonus):
    print(s, end = ', ')
print() 
    

### lambda
for s in filter(lambda x : x < 60, score):
    print(s, end = ', ') 
print() 


for s in map(lambda x : x / 2, score):
    print(s, end = ', ')
    