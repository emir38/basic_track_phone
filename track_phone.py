#!/usr/bin/env python3

import phonenumbers
import opencage
import folium
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode

key = 'ENTER-API_OF_OPEN_CAGE'

number = input("Enter number to geotrack (Include country code, Ex: +99 999 9999999): ")

parsenumber = phonenumbers.parse(number)
location = geocoder.description_for_number(parsenumber, "en")
service_provider = carrier.name_for_number(parsenumber, "en")

geocoder = OpenCageGeocode(key)

query = str(location)

results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")

print(number)
print(location)
print(service_provider)
print(lat, lng)
print("The map has been generated succesfully in the folder of this script")

