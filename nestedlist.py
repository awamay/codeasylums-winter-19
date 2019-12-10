# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:21:17 2019

@author: awani
"""

a =[1,2,3,[4,[5,8,9],8],6,7]

def solve(a,n):
    for i in a:
        if type(i)==list:
            solve(i,n+n)
        else:
            print(n,i)            
        
    
    
n=" "     
solve(a,n)

