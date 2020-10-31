#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:59:49 2019

@author: a.alex
"""

import math
dummy = "abin"
dummy = dummy.replace(" ","")
l = len(dummy)/2
if l%2!=0:
    middle_letters = dummy[int(l)]
else:

    middle_letters = dummy[int(l)-1]
if len(dummy)>5:
    print(dummy[0:2]+middle_letters*(len(dummy)-4)+dummy[-2:])

