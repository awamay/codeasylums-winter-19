# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 07:42:55 2019

@author: awani
"""

add = lambda x,y:x+y
x = [1,2,3,4]
y = [4,3,2,1]
z = list(map(add,x,y))
print(z)
