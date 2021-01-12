# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 10:09:26 2021

@author: 경진
"""

import statistics as st

score = [30, 40, 60, 70, 80, 90]

print(st.mean(score))
print(st.harmonic_mean(score))
print(st.median(score))
print(st.median_low(score))
print(st.median_high(score))