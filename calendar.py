# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 11:19:36 2021

@author: 경진
"""

import calendar

### 달력
print(calendar.calendar(2021))
print()
print(calendar.month(2021, 1))
print()


### weekday
week = ["월", "화", "수", "목", "금", "토", "일"]
day = calendar.weekday(2021, 8, 15)
print("광복절은 %s요일이다." % week[day])