# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 21:26:43 2025

@author: lujal
"""


A = [10, 20, 30, 40,50]
B = [60, 70, 80, 90, 20]
print("Before Swap:\nA=",A,"\nB=",B)

A[0], A[-1],B[0], B[-1] = B[-1], B[0],A[-1], A[0]
 

print("After Swap:")
print("A =", A)
print("B =", B)
