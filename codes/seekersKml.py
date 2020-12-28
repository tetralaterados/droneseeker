#seekersKml.py
# Code that reads the very last point of three 3 CSV:
# INPUTS: (seeker_blue_hist.csv,seeker_red_hist.csv, seeker_green_hist.csv) 
# and creates the corresponding KML points:
# OUTPUTS SeekerBlue.kml, SeekerGreen.kml, SeekerRed.kml. 
# In the name it includes the RSSI and the hour. The RSSI shown is a the average RSSI of a configurable number of last rows



import csv
import pandas as pd


last_points = 5


#Blue Seeker
data_initial = open("seeker_blue_hist.csv", "r")
data = csv.reader((line.replace('\0','') for line in data_initial), delimiter=",")
df = pd.DataFrame(data)
df.columns = ['time', 'lat','long','alt','rssi']
df1 = df.tail(last_points)
df1[["rssi"]] = df1[["rssi"]].apply(pd.to_numeric)
df2 = df.tail(1)
time = df2.time.values[0]
latitude = df2.lat.values[0]
longitude = df2.long.values[0]
altitude = df2.alt.values[0]
rssimean = str(df1["rssi"].mean())
rssimean = round(float(rssimean), 5)
rssimean = str(rssimean)

f = open('SeekerBlue.kml', 'w')
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<kml xmlns="http://earth.google.com/kml/2.0">\n')
f.write('<Folder>\n')
f.write('<Style id="icon_upc">\n')			
f.write('<IconStyle>\n')			
f.write('<Icon>\n')			
f.write('<href>drone_blue.png</href>\n')			
f.write('	</Icon>\n')			
f.write('</IconStyle>\n')			
f.write('</Style>\n')			
f.write('<Placemark>\n')	
f.write('<name>')
f.write(time)
f.write(', ')
f.write(rssimean)
f.write('</name>\n')
f.write('<styleUrl>#icon_upc</styleUrl>\n')
f.write('<description></description>\n')        
f.write('<Point>\n')
f.write('<altitudeMode>absolute</altitudeMode>\n')	
f.write('<coordinates>')
f.write(longitude)
f.write(',')
f.write(latitude)
f.write(',')
f.write(altitude)   	
f.write('</coordinates>\n')   			
f.write('</Point>\n')   
f.write('</Placemark>\n')   
f.write('</Folder>\n')   
f.write('	</kml>\n')   	
f.close()



#Red Seeker
data_initial = open("seeker_red_hist.csv", "r")
data = csv.reader((line.replace('\0','') for line in data_initial), delimiter=",")
df = pd.DataFrame(data)
df.columns = ['time', 'lat','long','alt','rssi']
df1 = df.tail(last_points)
df1[["rssi"]] = df1[["rssi"]].apply(pd.to_numeric)
df2 = df.tail(1)
time = df2.time.values[0]
latitude = df2.lat.values[0]
longitude = df2.long.values[0]
altitude = df2.alt.values[0]
rssimean = str(df1["rssi"].mean())
rssimean = round(float(rssimean), 5)
rssimean = str(rssimean)

f = open('SeekerRed.kml', 'w')
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<kml xmlns="http://earth.google.com/kml/2.0">\n')
f.write('<Folder>\n')
f.write('<Style id="icon_upc">\n')			
f.write('<IconStyle>\n')			
f.write('<Icon>\n')			
f.write('<href>drone_Red.png</href>\n')			
f.write('	</Icon>\n')			
f.write('</IconStyle>\n')			
f.write('</Style>\n')			
f.write('<Placemark>\n')	
f.write('<name>')
f.write(time)
f.write(', ')
f.write(rssimean)
f.write('</name>\n')
f.write('<styleUrl>#icon_upc</styleUrl>\n')
f.write('<description></description>\n')        
f.write('<Point>\n')
f.write('<altitudeMode>absolute</altitudeMode>\n')	
f.write('<coordinates>')
f.write(longitude)
f.write(',')
f.write(latitude)
f.write(',')
f.write(altitude)   	
f.write('</coordinates>\n')   			
f.write('</Point>\n')   
f.write('</Placemark>\n')   
f.write('</Folder>\n')   
f.write('	</kml>\n')   	
f.close()



#Green Seeker
data_initial = open("seeker_green_hist.csv", "r")
data = csv.reader((line.replace('\0','') for line in data_initial), delimiter=",")
df = pd.DataFrame(data)
df.columns = ['time', 'lat','long','alt','rssi']
df1 = df.tail(last_points)
df1[["rssi"]] = df1[["rssi"]].apply(pd.to_numeric)
df2 = df.tail(1)
time = df2.time.values[0]
latitude = df2.lat.values[0]
longitude = df2.long.values[0]
altitude = df2.alt.values[0]
rssimean = str(df1["rssi"].mean())
rssimean = round(float(rssimean), 5)
rssimean = str(rssimean)

f = open('SeekerGreen.kml', 'w')
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<kml xmlns="http://earth.google.com/kml/2.0">\n')
f.write('<Folder>\n')
f.write('<Style id="icon_upc">\n')			
f.write('<IconStyle>\n')			
f.write('<Icon>\n')			
f.write('<href>drone_green.png</href>\n')			
f.write('	</Icon>\n')			
f.write('</IconStyle>\n')			
f.write('</Style>\n')			
f.write('<Placemark>\n')	
f.write('<name>')
f.write(time)
f.write(', ')
f.write(rssimean)
f.write('</name>\n')
f.write('<styleUrl>#icon_upc</styleUrl>\n')
f.write('<description></description>\n')        
f.write('<Point>\n')
f.write('<altitudeMode>absolute</altitudeMode>\n')	
f.write('<coordinates>')
f.write(longitude)
f.write(',')
f.write(latitude)
f.write(',')
f.write(altitude)   	
f.write('</coordinates>\n')   			
f.write('</Point>\n')   
f.write('</Placemark>\n')   
f.write('</Folder>\n')   
f.write('	</kml>\n')   	
f.close()