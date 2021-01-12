# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 14:48:04 2021

@author: 경진
"""

import sys

print("버전 :", sys.version)
print("플랫폼 :", sys.platform)
if (sys.platform == "win32") :
    print(sys.getwindowsversion())
print("바이트 순서 :", sys.byteorder)
print("모듈 경로 :", sys.path)