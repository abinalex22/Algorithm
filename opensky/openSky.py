#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 09:33:01 2019

@author: a.alex
"""
import json
from time import gmtime, strftime
import numpy as np
import matplotlib.pyplot as plt

def access(observation,property_name):    
    return observation[property_name] #access property value from the observation

def flyingcount(observation):
    count =0
    countnotflying =0
    for each in observation:
        if str(each["altitude"])!="None": #cleaning the altitude value 
            if str(each["altitude"])!=0: # counting aircrafts that  are flying
                count+=1
        else:
            countnotflying +=1 # counting aircrafts that  are on ground altitude = 0
    return count,countnotflying

def countryList(observation):
    ListofCountry =[]
    for each in observation:
        if each["origin_country"] not in ListofCountry and each["origin_country"] != "":
            ListofCountry.append(each["origin_country"]) # storing all the name of  countries in a list
    return ListofCountry

def timestamp(observation,property_name): #observation is list of dictionaries and property_name is time_position
    listofts =[]
    for each in observation:
        if each[property_name]  is not None:
            each[property_name] = each[property_name]*0.3048
            print(each[property_name])
            listofts.append(each[property_name]) # storing all the time stamps in a list
    latest =strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime(max(listofts))) #latest flight 
    earliest = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime(min(listofts)))    #earliest flight
    return str(latest),str(earliest)


def histplot(observation,property_name):
    listofalt =[]
    for each in observation:
        if each[property_name]  is not None:
            listofalt.append(each[property_name])
    a = np.array(listofalt) 
    print("lowest altitude of flight is could be  below sea level",min(a)) # aircraft flying in places which are below sea level
    print("Highest altitude of flight is",max(a)) # high altitude flying aircraft
    
    plt.figure(figsize=(12,8)) #increasing the canvas of the graph
    plt.hist(a, bins = 100,rwidth =0.75)  #plotting for histogram with distribution for every 100m
    
    plt.xlabel(" Range of Altitude")
    plt.ylabel("Frequency distribution")
    plt.title("Altitude") 
    plt.show()

def main():
    infile = open("data/mediumOpenSkyData.json") # open json file
    data_String = infile.read() # read the content in string format
    data_json= json.loads(data_String) # convert the String into json
    infile.close()    # close json file
    
    listobservations =(data_json["states"]) # storing the list of  dictionaries
    val = access(listobservations[0],"altitude") #printing value of proprty 'altitude'  from first observation  here , since it is a list sending the first dictionary which is in 0th index
    print("printing value of proprty 'altitude'from first observation here %.2f \n\n"%val)
    
    noOfPlanesFlying,notflying = flyingcount(listobservations)
    print("Number of Planes Flying right now %i \n\n"%noOfPlanesFlying)
    #print("Number of Planes ",notflying) #I'm not printing this; remove tht hash from begining
    
    ListOfCountries = countryList(listobservations) #sending the list of all dictionaries
    print(sorted(ListOfCountries),"\n\n")
    
    latest,earliest =timestamp(listobservations,"time_position")    #sending the list of all dictionaries and property
    print("latest flight time: %s\nearliest flight time: %s"%(latest,earliest)) #printing the latest and earliest time of flight on the day
    
    histplot(listobservations,"altitude") # sending the list of all dictionaries and the property name here is  altitude

if __name__ == "__main__":
    # execute only if run as a script
    main()
# l_of_prop = ['icao24','callsign','time_position','time_velocity','longitude','latitude','altitude','on_ground','velocity','heading','vertical_rate','sensors']

