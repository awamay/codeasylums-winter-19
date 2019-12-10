# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 09:20:34 2019

@author: awani
"""

d = {1:[2,3,4], 2:[2,3], 3:6, 4:9}

ans = list(filter(lambda i:type(i)==list,d.values()))
print(len(ans))