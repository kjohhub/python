# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 10:28:37 2021

@author: 경진
"""

import os


    
def dumpdir(path):
    files = os.listdir(path);
    for f in files:
        fullpath = path + "\\" + f
        try:
            if os.path.isdir(fullpath):
                print("["+ fullpath +"]")
                dumpdir(fullpath)
            else:
                print("\t" + fullpath)
        except:
            pass
        
            
dumpdir("c:\\users\\경진\\python")