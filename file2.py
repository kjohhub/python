# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 09:44:33 2021

@author: 경진
"""

import shutil

def mycopy(a, b):
    f = open("live.txt", "rt")
    f2 = open("live2.txt", "wt")
    f2.writelines(f.readlines())
    f.close()
    f2.close()

shutil.copy("live.txt", "live2.txt")

