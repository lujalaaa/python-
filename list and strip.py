# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 19:02:11 2025

@author: lujala
"""

def list_and_split(words,to_be_removed):
    new_list=[w.strip() for w in words if w.strip()!=to_be_removed] #list condition
    print("original list:",words)
    print("new list:",new_list)

words=["apples", "   banana","mango","grapes"]

list_and_split(words, "banana")