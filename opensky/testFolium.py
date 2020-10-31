# -*- coding: utf-8 -*-
import folium
import json
import random
def mappy(listobservations):    
    count =1
    plane = folium.features.CustomIcon('plane.png',icon_size=(50,50))
    for each in listobservations:
        if each["longitude"]  is not None and each["latitude"]  is not None:
            if 43.55<each["latitude"]<43.68 and 1.30<each["longitude"]<1.55:
               print(each,"\n")
               folium.Marker( [each["latitude"] , each["longitude"]],icon=folium.Icon(icon=plane,color= random.choice(['red', 'blue', 'green', 'purple', 'orange', 'darkred', 'lightred', 'beige', 'darkblue', 'darkgreen'])), popup='<i>Plane %s from %s</i>'%(str(count),str(each["origin_country"]))).add_to(m)
               count+=1
                        
m= folium.Map(location=[43.6, 1.4],zoom_start=12)
folium.Marker( [43.5661107 , 1.474090], popup='<i>ISAE-Supaero</i>').add_to(m)
folium.Marker( [43.604696 , 1.445107 ], popup='<i>Toulouse Capitole</i>').add_to(m)
infile = open("data/mediumOpenSkyData.json") # open json file
data_String = infile.read() # read the content in string format
data_json= json.loads(data_String) # convert the String into json
listobservations =(data_json["states"])
mappy(listobservations)
m.save('myMap.html')



