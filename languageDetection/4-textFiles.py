# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 03:56:14 2019

@author: USER
"""

number_of_es = 0
# insert your code here
infile = open('data/austen-emma-excerpt.txt')
text = infile.read()
print(text)
for t in text:
    if t.count("e"):
        number_of_es+=1

# The following test should print True if your code is correct 
print(number_of_es == 78)