# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 11:45:10 2021

@author: 경진
"""

import random

for i in range(5):
    print(random.random())
    
    
for i in range(5):
    print(random.randint(0, 10))
    
    
for i in range(5):
    print(random.uniform(0, 100))


### choice    
food = ["짜장면", "짬뽕", "탕수육", "군만두"]
print(random.choice(food))

### suffle
print(food)
random.shuffle(food)
print(food)

### sample
print(random.sample(food, 2))

nums = random.sample(range(1, 45), 6)
nums.sort()
print(nums)



