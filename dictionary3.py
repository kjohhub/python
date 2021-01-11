# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 15:18:38 2021

@author: 경진
"""



song = """by the rivers of babylon, there we sat down
yeah we wept, when we remember zion.
when the wicked carried us away in captivity
required from us a song
now how shall we sing the lord's song in a strange land"""

alphabet = dict()

for c in song:
    if c.isalpha():
        c = c.lower()
        if c not in alphabet:
            alphabet[c] = 1
        else:
            alphabet[c] += 1
        
print(alphabet)

key = list(alphabet.keys())
key.sort()
for c in key:
    print(c, "=>", alphabet[c])
    
