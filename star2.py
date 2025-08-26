# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 20:05:47 2025

@author: lujal
"""

n=int(input("enter a number: "))
for i in range(1,n+1):
    for s in range(n-i):
       print(" ", end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    