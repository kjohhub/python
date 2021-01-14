# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 17:25:19 2021

@author: kjoh
@comment: 일급시민
"""

#%% funcvalue - 함수도 변수처럼 대입할수 있다.
def add(a, b):
    print(a + b)
    
plus = add
plus(1, 2)


#%% funcpara - 함수도 파라미터로 사용할수 있다.
def calc(op, a, b):
    op(a, b)
    
def add(a, b):
    print(a + b)

def multi(a, b):
    print(a * b)
    
calc(add, 1, 2)
calc(multi, 3, 4)


