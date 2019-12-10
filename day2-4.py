# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 19:57:57 2019

@author: awani
"""
t = int(input())
while t>0:
	n = int(input())
	c = 0
	c = n*(3*n+1)
	c = int(c/2)
	c = int(c%1000007)
	print(c,"\n")
	t=t-1
	
