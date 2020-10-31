#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:41:45 2019

@author: a.alex
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


author = Person("Maarten", 30)
computer = Person("Abin", 25)
print("My name is %s"%author.name)
print("My age is " + str(computer.age))
print("My name is " + author.name)
print("My age is " + str(author.age))