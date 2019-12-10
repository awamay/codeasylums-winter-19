# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 01:55:52 2019

@author: awani
"""

a = [2,3,56,23,14,23]
f=0
s=0
for i in range (0,6):
    if a[i]>f:
        f=a[i]

for i in range (0,6):
    if a[i]>s and a[i]<f:
        s=a[i]

print(s)