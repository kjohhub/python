# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 14:46:45 2021

@author: 경진
"""

### dic method
dic = { 'boy':'소년', 'scool':'학교', 'book':'책'}

print(dic.keys())
print(dic.values())
print(dic.items())

keylist = dic.keys()
for key in keylist:
    print(key)
    
    
dic2 = {'student':'학생', 'teacher':'선생님', 'book':'서적'}
dic.update(dic2)
print(dic)


### list to dictionary
li = [['boy', '소년'], ['scool', '학교'], ['book', '책']]
dic = dict(li)
print(dic)

