import csv
import os
import time
from datetime import datetime, timedelta, timezone, tzinfo
from pyephem_sunpath.sunpath import sunpos


#latitude = 52.006300
#longitude = 4.977895

#https://www.suncalc.org/#/52.0063,4.9779,18/2021.04.18/23:05/1/3

latitude = 52.00630
longitude = 4.97790


print (-time.timezone)
print (datetime.tzinfo)

thetime = datetime.now() 
lat = latitude
lon = longitude
tz = 2

alt, azm = sunpos(thetime, lat, lon, tz, dst=False)
print("Hoogte: ",alt)
print("Azimuth: ", azm)

















setting = []
value = []
settings2 = {}










with open("Settings.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile ,delimiter=';')
    for row in csvReader:
        setting.append(row[0])
        value.append(row[1])
        settings2 [row[0]] = row[1]
 

#print (int (settings2["Noorderbreedte"]) * 2)

class ScreenController:
    
    def setManualOff(self):
        return print ("Manual off")
        
        

scrFront = ScreenController()

#scrFront.setManualOff()
