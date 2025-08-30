# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 21:07:49 2025

@author: lujal
"""

import os 

# Current file path
old_name = "G:\\lujalaAI\\demo4.txt"

# New file name
new_name = "G:\\lujalaAI\\rename_by_python.txt"

# Rename the file
os.rename(old_name, new_name)

print(f"File renamed to: {new_name}")
