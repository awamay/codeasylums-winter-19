# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 00:53:39 2019

@author: awani
"""

ar = [1,-2,3,-4,5]
def update(a):
    for i in range(0,5):
        if a[i]>0 :
            a[i]=pow(int(a[i]),3)
        print(a[i])

update(ar)
            