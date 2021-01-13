# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 16:21:27 2021

@author: 경진
@comment: 클래스
"""

class Account:
    def __init__(self, balance):
        self.balance = balance
    def deposit(self, money):
        self.balance += money
    def withdraw(self, money):
        self.balance -= money
    def inquire(self):
        print("잔액은 %d입니다." % self.balance)
        
        
sinhan = Account(8000)
sinhan.deposit(1000)
sinhan.withdraw(6000)
sinhan.inquire()
