# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 15:34:22 2021

@author: 경진
"""


### exception
try:
    text = "89점"
    score = int(text)
    print("점수는 %d점 입니다." % score)
    
except ValueError as e:
    print(e)
    
except IndexError as e:
    print(e)
    
except (NameError, ZeroDivisionError, TypeError) as e:
    print(e)
    
### raise
def calcsum(n):
    if (n < 0):
        raise ValueError
    sum = 0
    for i in range(n+1):
        sum = sum + i
    return sum

try:
    print("~10 =", calcsum(10))
    print("~-5 =", calcsum(-5))
except ValueError:
    print("입력값이 잘못되었습니다.")
    
    
### finally
try:
    print("네트워크 접속")
    a = 2/0
    print("네트워크 통신 수행")
except:
    print("예외 발생")
finally:
    print("접속 해제")
print("작업 완료")


### assert
score = 128
assert score <= 100, "점수는 100이하 여야 합니다"
print(score)