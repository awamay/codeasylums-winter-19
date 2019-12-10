# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 18:27:32 2019

@author: awani
"""

s = "abcdefghijklmnopqrstuvwxyz"
ss = ["abcd","cdef","ghij","ghtfd","shfgg"]

ans = list(filter(lambda i:s.find(i)!=-1,ss))
print(ans)

