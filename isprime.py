# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 18:47:22 2025

@author: lujal
"""

"""program to find if a number is prime or not """
from sympy import isprime
n=int(input("enter a number:"))
if isprime(n):
    print("the number is prime")
else:
    print("the number is not prime")
