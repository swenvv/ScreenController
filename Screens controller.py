import csv
import os
import time
from datetime import datetime, timedelta, timezone, tzinfo
from pyephem_sunpath.sunpath import sunpos


# Read CSV file with settings
settings = {}

with open("Settings.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile ,delimiter=';')
    for row in csvReader:
        settings [row[0]] = row[1]
 

# Calculate Azimuth and Altitude of the sun

theTime = datetime.now() 
theUtcTime = datetime.utcnow()

lat = settings["latitude"]
lon = settings["longitude"]
tz = int(theTime.hour - theUtcTime.hour)

altitude, azimuth = sunpos(theTime, lat, lon, tz, dst=False)
print("altitude: ",altitude)
print("Azimuth: ", azimuth)


class ScreenController:
    def __init__(self, startAngle, endAngle, startAltitude, endAltitude):
        self.startAngle = startAngle
        self.endAngle = endAngle
        self.startAltitude = startAltitude
        self.endAltitude = endAltitude
  
    def setManualOff(self):
        return print ("Manual off")

    def ScreenInSunInReach(self):
        hit = 1
        if azimuth < self.startAngle:
            hit = 0
        if azimuth > self.endAngle:
            hit = 0
        if altitude < self.startAltitude:
            hit = 0
        if altitude > self.endAltitude:
            hit = 0
        return hit

scrFront = ScreenController(float(settings["startAngle"]), 
                            float(settings["endAngle"]),
                            float(settings["startAltitude"]), 
                            float(settings["endAltitude"]))

print ("In reach of the sun: ", scrFront.ScreenInSunInReach())


