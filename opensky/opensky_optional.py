#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:42:16 2019

@author: a.alex
"""
import json
import time
from opensky_api_ISAE import * 
import folium



    
def mappy(listobservations,myICAO):
    for each in listobservations:    
        folium.Marker( [each["latitude"] , each["longitude"]],icon=folium.Icon(icon='plane',color='orange'), popup='<i>Plane %s from %s</i>'%(str(count),str(each["origin_country"]))).add_to(m)
    
                        
def icao_values_of_ac(observation,property_name):  
    list_of_icao =[]
    for each in observation:
        if each[property_name] is not None:
            list_of_icao.append(each[property_name])
    return list_of_icao

def main():
    api = OpenSkyApi()
    json_string = api.get_states()
    data_json= json.loads(json_string)
    print(type(json_string))
    list_of_states =data_json["states"]
    
    myICAO = icao_values_of_ac(list_of_states,"icao24")
    print("value of icao24 for the plane that I'm going to track",myICAO)
    

    m= folium.Map(location=[43.6, 1.4],zoom_start=1)
    mappy(list_of_states,myICAO)
    m.save('optionalmymap.html')
    time.sleep(10)
    #parse json -> find the same icao
    
    #stop here
    
    

if __name__ == "__main__":
    # execute only if run as a script
    main()