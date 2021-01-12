# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 10:12:01 2021

@author: 경진
"""

import math
import turtle as t

t.penup()
t.goto(-720, 0)
t.pendown()
for x in range(-720, 720):
    t.goto(x, math.sin(math.radians((x)))*100)
t.done()