# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 14:18:09 2021

@author: 경진
"""

import time


### two return
def gettime():
    now = time.localtime()
    return now.tm_hour, now.tm_min

result = gettime()
print("지금은 %d시 %d분입니다" % (result[0], result[1]))


d, m = divmod(7, 3)
print("몫", d)
print("나머지", m)


### convert list
score = [88, 95, 70, 100, 99]
tu = tuple(score)
#tu[0] = 100
print(tu)
li = list(tu)
li[0] = 100
print(li)