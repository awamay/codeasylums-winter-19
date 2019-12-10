# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 08:56:01 2019

@author: awani
"""


x = ["aba","vhgfv","e","r","ertt"]

ans = list(filter(lambda i:len(i)>=2,x))
anss = list(filter(lambda s:s[0]==s[-1],ans))

print(len(anss))

