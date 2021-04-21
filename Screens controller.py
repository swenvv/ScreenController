import csv
import os
import time
from datetime import datetime, timedelta, timezone, tzinfo
from pyephem_sunpath.sunpath import sunpos


# Read CSV file with settings

settings = []

with open("Settings.csv", 'r') as file:
    csv_file = csv.DictReader(file,delimiter=';')
    for row in csv_file:
        settings.append(row)


# Class
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


testArray = 1

# Calculate Azimuth and Altitude of the sun

theTime = datetime.now() 
theUtcTime = datetime.utcnow()

lat = settings[testArray]["latitude"]
lon = settings[testArray]["longitude"]
tz = int(theTime.hour - theUtcTime.hour)

altitude, azimuth = sunpos(theTime, lat, lon, tz, dst=False)
print("altitude: ",altitude)
print("Azimuth: ", azimuth)



scrFront = ScreenController(float(settings[testArray]["startAngle"]), 
                            float(settings[testArray]["endAngle"]),
                            float(settings[testArray]["startAltitude"]), 
                            float(settings[testArray]["endAltitude"]))

print (settings[testArray]["Name"], " In reach of the sun: ", scrFront.ScreenInSunInReach())


