# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 11:17:36 2021

@author: kjoh
@comment: 클래스 데코레이터
"""

#%% class wrapper
class Outer:
    def __init__(self, func):
        self.func = func
    def __call__(self):
        print("-" * 20)
        self.func()
        print("-" * 20)

def inner():
    print("결과를 출력합니다.")
    
inner = Outer(inner)
inner()


#%% class decorator
@Outer
def inner():
    print("결과를 출력합니다.")
    
inner()