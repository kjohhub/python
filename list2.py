# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 11:06:31 2021

@author: 경진
"""

### 이차원 배열
lol = [[1,2,3], [4,5], [6,7,8,9]]
print(lol[0])
print(lol[2][1])
for sub in lol:
    for item in sub:
        print(item, end = ' ')
    print()
    


### 예제 
score = [
    [88, 76, 92, 98],
    [65, 70, 58, 82],
    [82, 80, 78, 88]
    ]

total = 0
totalsub = 0
for student in score:
    sum = 0
    for subject in student:
        sum += subject
    subject = len(student)
    print("총점 %d, 평균 %.2f" %(sum, sum/subject))
    total += sum
    totalsub += subject
    
print("전체평균 %.2f" %(total/totalsub))


### 리스트 컴프리헨션
# [수식 for 변수 in 리스트 if 조건]
nums = [n * 2 for n in range(1, 11)]
print(nums)
