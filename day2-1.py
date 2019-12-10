# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 10:11:42 2019

@author: awani
"""

d={"name":"awanika","branch":"ece","roll":"123"}
for i,j in d.items():
    print(i,j)
d.pop("branch")

1+(21*x)=3

lambda
map
filter
reduce
x = lambda a:a**2
l = [1,2,3,4]
y = lambda j,z:j+z
lis = list(map(x,l))
lis = list(filter(x,l))
lis = list(reduce(y,l))


t = input()
t = int(t)
def reverse(n):
	s=0
	while n>0:
		s=10*s + n%10
		n = int(n/10)
	return s

while t>=0:
	a=int(input())
	b=int(input())
	
	ans = reverse(reverse(a)+reverse(b))
	print(ans)
	t=t-1
