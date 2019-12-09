# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 01:11:39 2019

@author: awani
"""

a = input("enter: ")
a = int(a)

s=0
while(a>0):
    s = 10*s+a%10
    a = int(a/10)
    

while(s>0):
    t = s%10
    for i in range(1,t+1):
        print("hello"+str(i)," ",end="")
    print("\n")
    s = int(s/10)

