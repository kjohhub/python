# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 17:48:08 2021

@author: kjoh
@comment: 지역함수
"""

#%% local func - 지역함수 : 함수안의 함수
def calcsum(n):
    def add(a, b):
        return a + b
    
    sum = 0
    for i in range(n + 1):
        sum = add(sum, i)
    return sum

print("~10 =", calcsum(10))


#%% factory func - 함수가 함수를 만들어 리턴
def makeHello(message):
    def hello(name):
        print(message + "," + name)
    return hello

enghello = makeHello("Good Morning")
korhello = makeHello("안녕하세요")

enghello("Mr Kim")
korhello("홍길동")