# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 14:42:17 2021

@author: kjoh
"""

INCH = 2.54

def calcsum(n):
    sum = 0
    for num in range(n + 1):
        sum += num
    return sum


### import할때는 출되지 않는다
if __name__ == "__main__":
    print("인치 =", INCH)
    print("합계", calcsum(10))