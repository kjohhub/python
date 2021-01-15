# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:20:41 2021

@author: kjoh
"""

import turtle as t


#%% turtle
t.shape("turtle")

t.forward(100)
t.right(90)
t.forward(100)
t.done()


#%% updawn
t.shape("turtle")

t.speed(1)
t.forward(100)
t.up()
t.forward(100)
t.down()
t.forward(100)

t.done()


#%% draw circle
t.shape("turtle")

t.pensize(3)
t.color("blue")
t.bgcolor("green")
t.fillcolor("yellow")
t.begin_fill()
t.circle(100)
t.end_fill()
t.done()


#%% draw star
t.shape("turtle")


for a in range(5):
    t.forward(150)
    t.right(144)
    
t.done()