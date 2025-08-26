# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 19:56:32 2025

@author: lujal
"""

n=int(input("enter a number: "))
for i in range(1,n+1):
    for s in range(n-i):
       print(" ", end=" ")
    for j in range(0,2*i-1):
        print("*",end=" ")
    print()
    