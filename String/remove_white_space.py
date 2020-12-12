# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 11:10:17 2020

@author: RUHUL AMIN PARVEZ
"""

test_str = str(input("Enter line of string: "))

print("The original string is : " + test_str) 

result = " ".join(test_str.split()) 

# printing result 
print("The strings after extra space removal : " + str(result)) 

