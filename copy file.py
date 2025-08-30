# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 20:47:58 2025

@author: lujala
"""

# Original file path
source_file = "G:\\lujalaAI\\Ram.txt"

# Copy file path
destination_file = "G:\\lujalaAI\\Ram_copy.txt"

# Open the original file in read mode and the new file in write mode
with open(source_file, "r") as src:
    content = src.read()

with open(destination_file, "w") as dest:
    dest.write(content)

print("File copied successfully!")
