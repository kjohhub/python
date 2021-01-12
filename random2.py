# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 13:48:50 2021

@author: 경진
"""

import random


num = 0

while True:
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    

    question = "%d + %d ? " % (a, b)
    c = int(input(question))
    
    if c == 0:
        break
    elif a + b == c:
        print("정답입니다")
        num += 1
    else:
        print("오답입니다")
        
        
print("정답수는 %d개 입니다" % num)