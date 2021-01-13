# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 16:27:18 2021

@author: 경진
@comment: 클래스 상속
"""

class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def intro(self):
        print("%d살 %s입니다." % (self.age, self.name))
        
class Student(Human):
    def __init__(self, age, name, stunum):
        super().__init__(age, name)
        self.stunum = stunum
    def intro(self):
        super().intro()
        print("학번은 %d입니다" % self.stunum)
    def study(self):
        print("%s가 공부를 합니다" % self.name)
        
        
kim = Human(29, "김상형")
kim.intro()

lee = Student(34, "이승우", 930011)
lee.intro()
lee.study()