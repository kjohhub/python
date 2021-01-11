# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 14:30:04 2021

@author: 경진
"""

## 사전
dic = { 'boy':'소년', 'scool':'학교', 'book':'책'}
print(dic)


print(dic['boy'])
print(dic['book'])

print(dic.get('student'))
print(dic.get('student', '사전에 없는 단어입니다'))

if 'student' in dic:
    print("사전에 있는 단어입니다.")
else:
    print("사전에 없는 단어입니다.")
    

dic['boy'] = '남자애'
dic['girl'] = '소녀'
del dic['book']
del dic[2]
print(dic)