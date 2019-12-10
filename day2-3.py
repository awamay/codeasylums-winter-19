# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 19:59:25 2019

@author: awani
"""

l = [10, 20, 4, 45, 99] 
  
f=0 
s=0
  
for i in l: 
    if i>f: 
        s=f
        f=i
    else: 
        if i>s: 
            s=i
  
print(s)