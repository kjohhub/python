# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 10:24:26 2021

@author: 경진
"""

score = [88, 95, 70, 100, 99]
nums = [0,1,2,3,4,5,6,7,8,9]


### 리스트의 요소
print(score[0])
print(score[2])
print(score[-1])


### 요소분리 : 범위지정
print(nums[2:5])
print(nums[:4])
print(nums[6:])
print(nums[1:7:2])


### 리스트 assign
print(score[2])
score[2] = 55
print(score[2])


### 리스트 replace
nums[2:5] = [20, 30, 40]
print(nums)
nums[6:8] = [90, 91, 92,93,94]
print(nums)


### 리스트 제거
nums = [0,1,2,3,4,5,6,7,8,9]
nums[2:5] = []
print(nums)
del nums[4]
print(nums)

### 리스트 cat
list1 = [1,2,3,4,5]
list2 = [10, 11]
listadd = list1 + list2
print(listadd)
listmulti = list2 * 3
print(listmulti)