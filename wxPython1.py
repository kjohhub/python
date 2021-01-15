# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:43:41 2021

@author: kjoh
@comment: wxPython
"""

import wx


#%% wxApp
app = wx.App()
frame = wx.Frame(None)

size = wx.Size(600, 400)
frame.SetSize(size)
pos = wx.Point(100, 100)
frame.SetPosition(pos)
color = wx.Colour(0, 0, 255, 0)
frame.SetBackgroundColour(color)
frame.SetTitle("파이썬으로 만든 윈도우")
frame.SetWindowStyle(wx.DEFAULT_FRAME_STYLE & ~wx.RESIZE_BORDER)


def OnMouseClick(event):
    message = "(%d, %d)를 클릭했습니다." % (event.x, event.y)
    wx.MessageBox(message, "알림", wx.OK)
frame.Bind(wx.EVT_LEFT_DOWN, OnMouseClick)

def OnKeyDown(event):
    message = "%d 키를 눌렀습니다." % event.KeyCode
    wx.MessageBox(message, "알림", wx.OK)
frame.Bind(wx.EVT_KEY_DOWN, OnKeyDown)


frame.Show(True)
app.MainLoop()


