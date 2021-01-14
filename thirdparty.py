# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 16:04:49 2021

@author: kjoh
"""


#%%
import wx


app = wx.App()
frame = wx.Frame(None, 0, "파이썬 만세")

frame.Show(True)
app.MainLoop()


#%%
from urllib import request
import bs4

target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
soup = bs4.BeautifulSoup(target, "html.parser")

for city in soup.select("location"):
    name = city.select_one("city").string
    wf = city.select_one("wf").string
    tmn = city.select_one("tmn").string
    tmx = city.select_one("tmx").string
    print("%s : %s(%s ~ %s)" % (name, wf, tmn, tmx))