# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 17:34:33 2021

@author: 경진
@comment: 연산자 메소드, 특수 메소드
"""

class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def __eq__(self, other):
        return self.age == other.age and self.name == other.name
    def __str__(self):
        return "이름 %s, 나이 %d" %(self.name, self.age)
    def __len__(self):
        return len(self.name)


kim = Human(29, "김상민")
sang = Human(29, "김상민")
moon = Human(44, "문종민")

print(kim == sang)
print(kim == moon)
print(kim)
print(len(kim))