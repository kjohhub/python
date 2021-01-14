# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 17:07:13 2021

@author: kjoh
@comment: generator
"""



#%% generator
def seqgen(data):
    for index in range(0, len(data), 2):
        yield data[index:index+2]
        
solarterm = seqgen("입춘우수경칩춘분청명곡우입하소만망종하지소서대서")
for k in solarterm:
    print(k, end = ",")


#%% gen expr
data = "입춘우수경칩춘분청명곡우입하소만망종하지소서대서"
for k in (data[index: index + 2] for index in range(0, len(data), 2)):
    print(k, end = ",")


#%% range gen
for n in [i for i in range(100)]:
    print(n, end = ",")
print("")
for n in (i for i in range(100)):
    print(n, end = ",")
