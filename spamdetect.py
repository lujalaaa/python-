# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 19:05:51 2025

@author: lujal
"""

#list of spam comments
spam={"make a lot of money","Subscribe this","click this"}
#taking user's comment 
comment=(input("Enter a comment : "))
#checking if comment is spam 

detected=False;
for word in spam: #goes thru each item in spam and calls it word 
    if word.lower() in comment.lower(): #changing everything to lowercase to make it easier 
        detected=True
        break; 
    
if detected:
    print(f"{comment} is spam.")
else:
    print("this is fine") 