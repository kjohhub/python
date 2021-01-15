# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 11:30:07 2021

@author: kjoh
"""


#%% eval
result = eval("2 + 3 * 4")
print(result)

a = 2
print(eval("a + 3"))

city = eval("['seoul', 'osan', 'suwon']")
for c in city:
    print(c, end = ', ')
    
    

#%% eval : simple calc
import math # ex) math.qrt(2)

while True:
    try:
        expr = input("수식을 입력하세요(끝낼때: 0) : ")
        if expr == '0':
            break
        print(eval(expr))
    except:
       print("수식이 잘못되었습니다.") 
    
    
#%% repr
print(repr(1234), end = ',')
print(repr(3.14), end = ',')
print(repr(['seoul', 'osan', 'suwon']), end = ',')
print(repr('korea'))


#%%% repreval
intexp = repr(1234)     # '1234'
intvalue = eval(intexp) # 1234
print(intvalue)

strexp = repr('korea')  
strvalue = eval(strexp)
print(strvalue)


#%% class repr
class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def __str__(self):
        return "이름 %s, 나이 %d" % (self.name, self.age)
    def __repr__(self):
        return "Human(%d, '%s')" % (self.age, self.name)
    
    
kim = Human(29, '김상형')
print(kim)
kimexp = repr(kim)
kimcopy = eval(kimexp)
print(kimcopy)    



    