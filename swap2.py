# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 21:18:40 2025

@author: lujala
"""

A = [10, 20, 30, 40,50]
B = [60, 70, 80, 90, 20]
print("Before Swap:\nA=",A,"\nB=",B)
# Swap first two elements
A[:2], B[:2] = B[:2], A[:2]

# Swap last two elements
A[-2:], B[-2:] = B[-2:], A[-2:]
print("After Swap:")
print("A =", A)
print("B =", B)
