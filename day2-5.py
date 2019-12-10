# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 19:55:36 2019

@author: awani
"""

def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        r=[]
        
        while(n>0):
            r.append(n%10)
            n = int(n/10)
        s=0
        pr=1
        for i in r:
            s=s+i
            pr=pr*i
            
        return pr-s