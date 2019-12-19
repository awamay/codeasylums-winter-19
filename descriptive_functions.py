#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 18:25:39 2019

@author: awanika
"""

def mean(a):
    sum=0
    for i in (0,len(a)):
        sum = sum+a[i]
        
    avg = sum/len(a)
    return avg

def variance(a):
    x = mean(a)
    sum=0
    for i in range(0,len(a)):
        sum = sum + pow((a[i]-x),2)
        ans = sum/len(a)
    return ans

def stddev(a):
    ans = variance(a)
    std = pow(ans,0.5)
    return std

def median(a):
    a.sort_values()
    x = len(a)
    if(x%2==1):
        ans = a[(x//2)]
    else if(x%2==0):
        ans = a[(x/2)] + a[(x/2) - 1]
        ans = ans/2
    
    return ans


from collections import Counter
def mode(a):
    n = len(a)   
    data = Counter(a) 
    get_mode = dict(data) 
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))] 
          
    return mode 
        
       
    

def covariance(a,b):
    sum = 0
    x = mean(a)
    y = mean(b)
    for i in range(0,len(a)):
        sum = sum + (a[i]-x)*(b[i]-y)
    covar = sum/len(a)
    
def correlation(a,b):
    ans = covar(a,b)/(stddev(a)*stddev(b))
    return ans


#median function for IQR
def median(a,l,r): 
    n = r-l+1
    n = (n+1) // 2 - 1
    return n + l 
  
# Function to calculate IQR 
def IQR(a):   
    n = len(a)
    a.sort_values()   
    Q2 = median(a, 0, n) 
    Q1 = a[median(a, 0, Q2)] 
    Q3 = a[median(a, Q2 + 1, n)] 
    return (Q3 - Q1) 

    
    

def percentile(a,x):
    np.sort(a)
    ans = x*100/len(a)
    

def skewness(a):
    sum=0
    x = mean(a)
    for i in range(0,len(a)):
        sum = sum + pow((a[i]-x),3)
    sum = sum/(len(a)-1)
    s = stddev(a)
    ans = sum/pow(s,3)
    return ans
    

def coeffofvar(a):
    sd = stddev(a)
    mn = mean(a)
    ans = sd/mn
    return ans


    


    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        