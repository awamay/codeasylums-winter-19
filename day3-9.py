# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 18:41:45 2019

@author: awani
"""

def check(n):
    c=0
    d = int(len(n)/2)
    for i in range(0,d):
        if n[i]!=n[-i-1]:
            c=1
    if c==1:
        return False
    else:
        return True
    
    
q = ["nhu","abhba","baaab","abs","aabaa"]
ans = list(filter(lambda i:check(i),q))
print(ans)
    
    


    
            
            