# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:32:17 2021

@author: kjoh
"""

import turtle as t


#%% free line
def draw(head, dist):
    t.setheading(head)
    t.forward(dist)
    
def toleft():
    draw(180, 15)
    
def toright():
    draw(0, 15)
    
def toup():
    draw(90, 15)
    
def todown():
    draw(270, 15)
    
def move(x, y):
    t.up()
    t.setpos(x, y)
    t.down()
    
t.shape("turtle")
t.onkeypress(toleft, "Left")
t.onkeypress(toright, "Right")
t.onkeypress(toup, "Up")
t.onkeypress(todown, "Down")
t.onscreenclick(move)
t.listen()
t.done()



#%% free line2
def draw(x, y):
    t.setpos(x, y)
    
def move(x, y):
    t.up()
    t.setpos(x, y)
    t.down()
    
t.shape("turtle")
t.speed(0)
t.pensize(3)
t.onscreenclick(draw)
t.onscreenclick(move, 3)
t.onkeypress(lambda : t.color("red"), "r")
t.onkeypress(lambda : t.color("green"), "g")
t.onkeypress(lambda : t.color("blue"), "b")
t.onkeypress(lambda : t.color("black"), "k")
t.onkeypress(lambda : t.pensize(1), "1")
t.onkeypress(lambda : t.pensize(3), "3")
t.onkeypress(lambda : t.pensize(5), "5")
t.listen()
t.done()



