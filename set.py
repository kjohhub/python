# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 15:43:05 2021

@author: 경진
"""


### set
asia = {'korea', 'china', 'japan', 'korea'}
print(asia)


print(set('sanghyung'))
print(set([12, 34, 56, 78]))
print(set(("신지희", "한주완", "김태륜")))
print(set({'boy':'소년', 'school':'학교', 'book':'책'}))


asia.add('vietnam')
print(asia)
asia.remove('japan')
print(asia)
asia.update({'singapore', 'hongkong', 'korea'})
print(asia)


### 집합연산
twox = {2, 4, 6, 8, 10, 12}
threex = {3, 6, 9, 12, 15}

print("교집합", twox & threex)
print("합집합", twox | threex)
print("차집합", twox - threex)
print("차집합", threex - twox)
print("배타적 차집합", twox ^ threex)


### 부분집합
mammal = {'코끼리', '고릴라', '사자', '고래', '사람', '원숭이', '개'}
primate = {'사람', '원숭이', '고릴라'}

print(primate <= mammal)
print(primate < mammal)
print(primate <= primate)
print(primate < primate)