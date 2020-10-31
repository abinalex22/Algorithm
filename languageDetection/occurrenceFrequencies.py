# -*- coding: utf-8 -*-
"""
Created on "09-09-2019"
@author: "Abin Alex"
"""
# PROBLEM : find the occurence frequencies of the letters of the alphabet in the following text


# We can decompose the problem as follows :
#   1- create a dictionary containing the letters with the occurrences equal to 0 
#   2- for each letter in the text, increment the corresponding entry of the dictionary
#   3- normalize the values of the dictionary in order to have frequencies (the sum is equal to 1)

import re
text = "I WENT AND CALLED, BUT GOT NO ANSWER. ON RETURNING, I WHISPERED TO CATHERINE THAT HE HAD HEARD A GOOD PART OF WHAT SHE SAID, I WAS SURE; ANDTOLD HOW I SAW HIM QUIT THE KITCHEN JUST AS SHE COMPLAINED OF HERBROTHER'S CONDUCT REGARDING HIM.  SHE JUMPED UP IN A FINE FRIGHT, FLUNG HARETON ON TO THE SETTLE, AND RAN TO SEEK FOR HER FRIEND HERSELF; NOT TAKING LEISURE TO CONSIDER WHY SHE WAS SO FLURRIED, OR HOW HER TALK WOULD HAVE AFFECTED HIM.  SHE WAS ABSENT SUCH A WHILE THAT JOSEPH PROPOSED WE SHOULD WAIT NO LONGER.  HE CUNNINGLY CONJECTURED THEY WERE STAYING AWAY IN ORDER TO AVOID HEARING HIS PROTRACTED BLESSING."
print(text)

# letters
letters ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Creating a empty dict and initiliazing keys of alphabets with value as 0

  
# removing spaces and special characters from text
text_with_alpha = re.sub('[^A-Z]+', '', text)

# count of each alphabet
letterbox= {}
for l in letters:
    letterbox[l] = text_with_alpha.count(l)
print("\n*************the dict values************\n",letterbox.items(),"\n****************************************\n" )
# normalize the count values so that the sum of frquencies = 0
v=list(letterbox.values())
k=list(letterbox.keys())
print("max repeated alphabet is",k[v.index(max(v))], letterbox[k[v.index(max(v))]],"times")

normalizer =1/float(sum(v))
for l in letterbox:
    letterbox[l] = letterbox[l]*normalizer
maxV = max(letterbox.values())
minV = min(letterbox.values())
v=list(letterbox.values())
print( "after normalization",k[v.index(max(v))],max(v))
print ("sum of frequencies", sum(v))

