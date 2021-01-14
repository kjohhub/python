# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 14:26:44 2021

@author: kjoh
"""

INCH = 2.54

def calcsum(n):
    sum = 0
    for num in range(n + 1):
        sum += num
    return sum

### import 했을때 출력된다
print("인치 =", INCH)
print("합계 =", calcsum(10))
