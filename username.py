# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 19:19:28 2025

@author: lujal
"""
""" WAP  to check if a username contains less than 10 characters or not """


username=input("Enter username: ")
if len(username)<10:
    print("username contains less than 10 characters")
else:
    print("username contains more than 10 characters")