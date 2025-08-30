# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 20:15:59 2025

@author: lujala
"""
#opening in read mode to get content 
with open("G:\\lujalaAI\\demo3.txt","rt") as f :
          content=f.read()
        

censor=["donkey","monkey","ass","pig"]

new_content = content
for word in censor :
    censored="#"*len(word)
    new_content=new_content.replace(word,censored)


#opening the word in write mode to overwrite
with open("G:\\lujalaAI\\demo2.txt","wt") as f :
          f.write(new_content)
        
print("replacement done")
print(new_content)        