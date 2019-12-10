# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 01:27:51 2019

@author: awani
"""

n = int(input("enter number: "))
n1=n
s=0
while(n>0):
    s = 10*s + n%10
    n = int(n/10)

if s==n1:
    print("yes")
else:
    print("no")
