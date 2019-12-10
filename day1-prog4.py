# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 01:21:00 2019

@author: awani
"""

n=int(input("enter: "))
if(n%6==0):
    print("window")
if(n%6==1):
    print("window")
if(n%6==2):
    print("middle")
if(n%6==3):
    print("aisle")
if(n%6==4):
    print("aisle")
if(n%6==5):
    print("middle")
    
print(n+6)