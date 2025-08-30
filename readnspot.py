# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 19:47:22 2025

@author: lujal
"""


def read_n_find():
    with open("G:\\lujalaAI\\demo1.txt","rt") as f :
        content=f.read()
        if "twinkle" in content:
            print("file contains word twinkle")
            
read_n_find()
