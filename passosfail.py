# -*- coding: utf-8 -*-
"""
Created on Sun Aug 10 14:04:12 2025

@author: lujala
"""
'''wap to find out whether a student is failed or pass
 if it requires total 40% and at least 33% in each subject 
to pass Assume three subject and 
take marks as an input from user '''
# let us assume there are 3 subjects 
Math=eval(input('enter marks of maths: '))
Science=eval(input('enter marks of science: '))
English=eval(input('enter marks of English: '))

total=Math+Science+English
print("total marks is",total)
#assume full marks is 100 
percentage=total/3;
if(Math>=33 and Science>=33 and English>=33 and percentage>=40):
    print("student is pass")
else:
    print("student is fail")
