# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 10:16:52 2021

@author: kjoh
@comment: 함수 데코레이터
"""


#%% wrapper
def inner():
    print("결과를 출력합니다.")
    
def outer(func):
    print("-" * 20)
    func()
    print("-" * 20)
    
outer(inner)


#%% wrapper2
def inner():
    print("결과를 출력합니다.")
    
def outer(func):
    def wrapper():
        print("-" * 20)
        func()
        print("-" * 20)
    return wrapper


inner = outer(inner)
inner()


#%% decorater
def outer(func):
    def wrapper():
        print("-" * 20)
        func()
        print("-" * 20)
    return wrapper

@outer
def inner():
    print("결과를 출력합니다.")

inner()


#%% tag decorator
def div(func):
    def wrapper():
        return "<div>" + str(func()) + "</div>"
    return wrapper

def para(func):
    def wrapper():
        return "<p>" + str(func()) + "</p>"
    
    return wrapper

@div
@para
def outname():
    return "김상형"

@para
@div
def outage():
    return 29

print(outname())
print(outage())


#%% deco arg
from functools import wraps

def para(func):
    @wraps(func)    # 함수의 정보를 유지
    def wrapper(*args, **kwargs):
        return "<p>" + str(func(*args, **kwargs)) + "</p>"
    
    return wrapper

@para
def outname(name):
    return "이름:" + name + "님"

@para
def outage(age):
    return "나이:" + str(age)

@para
def outinfo(name, age):
    return "%s(%d)님" % (name, age)


print(outname("김상형"))
print(outage(29))
print(outinfo("김상형", 29))
print(outname.__name__)
