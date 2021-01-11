# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 16:28:35 2021

@author: 경진
"""

#enumerate
score = [88, 95, 70, 100, 99]

for no, s in enumerate(score, 1):
    print("%d번 학생의 점수 : %d" %(no, s))
print()
    

### zip
yoil = ["월", "화", "수", "목", "금", "토", "일"]
food = ["갈비탕", "순대국", "칼국수", "삼겹살"]
menu = zip(yoil, food)
for y, f in menu:
    print("%s요일 메뉴 : %s" %(y, f))
print()    
    
    
### any & all
adult = [True, False, True, False]
print(any(adult))
print(all(adult))

