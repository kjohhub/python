# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 17:11:53 2021

@author: 경진
@comment: 클래스 데커레이터
"""

class Date:
    def __init__(self, month):
        self.__month = month
    def getmonth(self):
        return self.__month
    def setmonth(self, month):
        if 1 <= month <= 12:
            self.__month = month
    month = property(getmonth, setmonth)
    
    
today = Date(8)
today.__month = 3       # 막을수는 없다

print(today.month)
print(today.__month)

        
        