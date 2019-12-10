# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 19:50:09 2019

@author: awani
"""
def gradingStudents(grades):
    # Write your code here
    b=[]
    for i in grades:
        if i>=38:
            t = int(i/5)
            d = 5*(t+1)-i
            if d<3:
                b.append(5*(t+1))
            else:
                b.append(i)
        else:
            b.append(i)

    return b

