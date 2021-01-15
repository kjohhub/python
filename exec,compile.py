# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 13:26:21 2021

@author: kjoh
"""


#%% exec
exec("value = 3")
print(value)


#%% exec2
for n in range(10):
    exec("""
for i in range(5):
    print(i, end = ',')
print()
    """)
    


#%%% compile
code = compile("""
for i in range(5):
    print(i, end = ',')
print()
""", '<string>', 'exec')

for n in range(10):
    exec(code)