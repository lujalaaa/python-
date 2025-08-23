# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 16:03:41 2025

@author: lujal
"""

'''A spam comment is defined as the text containing the following words 
"make a lot od Money",
"Subscribe this","click this ". WAP to detect this spam '''

#list of spam comments
spam={"make a lot of money","Subscribe this","click this"}
#taking user ko comment 
comment=(input("Enter a comment : "))
#checking if comment is spam 
if any(word.lower() in comment.lower() for word in spam):
    print(f"{comment} is prohibited.")
else:
    print("this is fine")