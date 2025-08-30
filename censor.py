# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 19:56:24 2025

@author: lujala
"""
#opening in read mode to get content 
with open("G:\\lujalaAI\\demo2.txt","rt") as f :
          content=f.read()
        
#replacement
new_content=content.replace("donkey","######")

#opening the word in write mode to overwrite
with open("G:\\lujalaAI\\demo2.txt","wt") as f :
          content=f.write(new_content)
        
print("replacement done")
print(new_content)        