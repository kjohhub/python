# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 10:14:08 2021

@author: 경진
"""

import time

print(time.time())

t = time.time()
print(time.ctime(t))

print(time.localtime(t))


now = time.localtime()
print("%d년 %d월 %d일" % (now.tm_yday, now.tm_mon, now.tm_mday))
print("%d:%d:%d" % (now.tm_hour, now.tm_min, now.tm_sec))


import datetime

now = datetime.datetime.now()
print("%d년 %d월 %d일" % (now.year, now.month, now.day))
print("%d:%d:%d" % (now.hour, now.minute, now.second))



### ellapse
import time

start = time.time()
for a in range(1000):
    print(a)
end = time.time()

print(end - start)


### sleep
print("안녕하세요")
time.sleep(5)
print("밤에 성시경이 두명 있으면 뭘까요?")
time.sleep(10)
print("야간 투시경입니다.")