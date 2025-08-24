# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 18:05:50 2025

@author: lujala
"""

'''WAP to calculate grade of student from his marks from the following scheme 
90-100->A+ Excellent
80-90->A
70-80->B
60-70->C
50-60->D
0-50 ->F'''
marks=eval(input("Enter your marks: "))
'''Python dictionaries allow us to associate a value to a unique key, and then to quickly access this value'''
grade={
       range(90,100):"A+",
       range(80,90):"A",
       range(70,80):"B",
       range(60,70):"C",
       range(50,60):"D",
       range(0,50):"F",
       }
for key,value in grade.items() :
    if marks in key:
        print("Grade:",value) 
        break 
    