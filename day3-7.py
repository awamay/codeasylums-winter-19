# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 09:32:59 2019

@author: awani
"""
from functools import reduce

d = {1:23,2:2,3:34,4:54}

v = d.values()
avg = reduce((lambda x,y:x+y),v)
avg = avg/len(v)

#sq = lambda x:avg
#ans = dict(map(sq,d.keys()))
#
#print(ans)

for i in d:
    d[i]=avg
    
print(d)