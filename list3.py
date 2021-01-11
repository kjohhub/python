# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 11:27:43 2021

@author: 경진
"""

### 리스트 insert
nums = [1, 2, 3, 4]
nums.append(5)
nums.insert(2, 99)
print(nums)


### 리스트 insert range
nums = [1, 2, 3, 4]
nums[2:2] = [90, 91, 92]
print(nums)
# 위와 다르다. 3자리에 리스트가 들어감
nums = [1, 2, 3, 4]
nums[2] = [90, 91, 92]
print(nums)


### extend
list1 = [1, 2, 3, 4, 5]
list2 = [10, 11]
list1.extend(list2)
print(list1)


### 리스트 삭제
score = [88, 95, 70, 100, 99, 80, 78, 50]
score.remove(100)
print(score)
del(score[2])
print(score)
score[1:4] = []
print(score)