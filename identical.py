# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 20:58:18 2025

@author: lujala
"""
# File paths
file1 = "G:\\lujalaAI\\Ram.txt"
file2 = "G:\\lujalaAI\\Ram_copy.txt"

# Open both files and read their content
with open(file1, "r") as f1, open(file2, "r") as f2:
    content1 = f1.read()
    content2 = f2.read()

# Compare the contents
if content1 == content2:
    print("The files are identical.")
else:
    print("The files are NOT identical.")

