#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 16:12:26 2019

@author: a.alex
"""
import re, math

#This function opens the book 
def readText(book):
    infile = open("data/"+book) # open
    myText = infile.read().lower()  # read and store in myText
    re.sub('[^a-z]+', '', myText) # replace anything other than small case alphabetets with "" so only small case leters left
    infile.close()
    return myText # myText now only contains alphabets in small case

# normalize the probability distribution sum of frequencies of all alphabets= 1
def normalizeSumTo(letterbox): # letterbox is a dictionary passed as a parameter
    v = letterbox.values()
    normalizer =1/float(sum(v))
    for l in letterbox:
        letterbox[l] = letterbox[l]*normalizer #modyfying values 
    return letterbox
        
#calculate frequencies of each alphabets
def counter(text_to_search):
    letterbox= {}
    letters = "abcdefghijklmnopqrstuvwxyz"
    for l in letters:
        letterbox[l] = text_to_search.count(l) # count for each alphabets and store in as  e.g. letterbox[a]= 374
    letterbox = normalizeSumTo(letterbox)
    return letterbox

    
#compare two languages and calculating
def Kullback_Leibler_Divergence(P,Q): # passing 2 dictionary of languages with the probability (normalized) frequency distribution
    d1 = 0
    d2 = 0
    for a in "abcdefghijklmnopqrstuvwxyz":
        if Q[a]!= 0.0 and P[a]!= 0.0:
            d1 += P[a]*math.log2(P[a]/Q[a])
            d2 += Q[a]*math.log2(Q[a]/P[a])
    avg =(d1 + d2)/2
    return math.fabs(avg) # returns the average of divergence values between two languages
    
  
# compares all the languages and calculate the divergence of the texts of each book
def languagecomparison():
    
    library = {} 
    myBooks = { #sample space
            "wutheringHeights.txt": "English",
            "MadameBovary.txt" : "French",
            "donQuijote.txt":"Spanish",
            "kritikDerReinenVernunft.txt":"German"
            }
    for NameOfBook in myBooks:
        onlyAlphText = readText(NameOfBook)
        language = myBooks[NameOfBook]
        library[language] = counter(onlyAlphText) # stores the counts of alphabets and store it in library based on its language
    lang = ["English","French","Spanish","German"]    
    for l in range(0,3): 
        for m in range(l+1,4):
            avg = Kullback_Leibler_Divergence(library[lang[l]],library[lang[m]]) # stores it in the local variable avg
            print ("avergage divergence of ", lang[l],lang[m], "is", str(avg), "\n")
    
   
# compares a unknown text with known values and shows the diverrgence values 
def languagedetector(newbook):
    print("****Testing for %s ****"%(newbook))
    library = {}
    myBooks = {
            "wutheringHeights.txt": "English",
            "MadameBovary.txt" : "French",
            "donQuijote.txt":"Spanish",
            "kritikDerReinenVernunft.txt":"German"
            }
    myBooks[newbook] = "Unknown Language"    
    for NameOfBook in myBooks:
        onlyAlphText = readText(NameOfBook)
        language = myBooks[NameOfBook]
        library[language] = counter(onlyAlphText) # stores the counts of alphabets and store it in library based on its language
    
    uk=[]
    lang = ["English","French","Spanish","German"]    
    for l in range(0,4): # runs the divergence for the new book language with the known languages
            avg = Kullback_Leibler_Divergence(library[lang[l]],library["Unknown Language"])
            uk.append(lang[l]+" "+str(avg))
            print ("avergage divergence of ", lang[l], "Unknown Language", "is", str(avg), "\n")
    print("Based on Comparison of divergence from previously known languages For %s the Unknown language is the least divergence combination %s"%(newbook,min(uk)))


print("********************language Comparison*****************")
languagecomparison()
print("********************language detector*******************")
# Test Book
languagedetector("austen-emma.txt")

