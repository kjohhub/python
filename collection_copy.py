# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 17:21:42 2021

@author: 경진
"""

import copy

### var copy
a = 3
b = a
print ("a = %d, b = %d" % (a, b))
a = 5
print ("a = %d, b = %d" % (a, b))


### 대입 : List의 사본을 만들지 않음
list1 = [1, 2, 3]
list2 = list1
list2[1] = 100

print(list1)
print(list2)


### swallow copy : List의 사본을 만듬
list1 = [1, 2, 3]
list2 = list1.copy()
list2[1] = 100

print(list1)
print(list2) 


### swallow copy : 내부의 list까지 사본을 만들지 않는다
list0 = ['a', 'b']
list1 = [list0, 1, 2]
list2 = list1.copy()

list2[0][1] = 'c'

print(list1)
print(list2)


### deep copy : 내부의 list까지 사본을 만든다
list0 = ['a', 'b']
list1 = [list0, 1, 2]
list2 = copy.deepcopy(list1)

list2[0][1] = 'c'

print(list1)
print(list2)


### is 연산자 : 같은 객체를 가르키고 있는지
list1 = [1, 2, 3]
list2 = list1
list3 = list1.copy()

print("1 == 2", list1 is list2)
print("1 == 3", list1 is list3)
print("2 == 3", list2 is list3)
