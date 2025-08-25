# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 18:07:32 2025

@author: lujala
"""


# factorial program
n = int(input("Enter a number:"))
fact = 1
for i in range(n,1,-1):      
    fact = fact*i
print(fact)