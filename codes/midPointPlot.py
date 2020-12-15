#midPointPlot.py
# Code that reads a configurable number of last rows of
# INPUTS:   midPointHist.csv
# and creates a KML with a spline (in the ground )
# OUTPUTS midPointHist.kml

import csv
import pandas as pd


last_points = 3

#Mid Point loading
data_initial = open("midpointHist.csv", "r")
data = csv.reader((line.replace('\0','') for line in data_initial), delimiter=",")
df = pd.DataFrame(data)
df.columns = ['latmean', 'longmean','timeBlue','timeGreen','timeRed']
df = df.tail(last_points)


#Mid Point Spline
f = open('midPointHist.kml', 'w')
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
f.write("	<Document>\n")
f.write("	<name>Mid Point Path</name>\n")
f.write('	<Style id="style1">\n')
f.write("		<LineStyle>\n")
f.write("			<color>64B40014</color>\n")
f.write("			<width>4</width>\n")
f.write("		</LineStyle>\n")
f.write("		<PolyStyle>\n")
f.write("			<color>5aFFFFFF</color>\n")
f.write("		</PolyStyle>\n")
f.write("	</Style>\n")
f.write("		<Placemark>\n")
f.write("			<name> Mid Point Path </name>\n")
f.write("			<styleUrl>#style1</styleUrl> \n")
f.write("   		<LineString>\n")
f.write("   		<extrude>1</extrude>\n")
#f.write("   		<tessellate>1</tessellate>\n")
f.write("   		<altitudeMode>clampToGround</altitudeMode>\n")
f.write("			<coordinates>")
for index, row in df.iterrows():
  	f.write("			"+row['longmean']+","+row['latmean']+"\n")
f.write("			</coordinates>\n")
f.write("			</LineString>\n")
f.write("		</Placemark>\n")
f.write("</Document>")
f.write("</kml>")
f.close()



#Mid Point point
df = df.tail(1)
latitude = df.latmean.values[0]
latitude = round(float(latitude), 5)
latitude = str(latitude)
longitude = df.longmean.values[0]
longitude = round(float(longitude), 5)
longitude = str(longitude)
f = open('midPoint.kml', 'w')
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<kml xmlns="http://earth.google.com/kml/2.0">\n')
f.write('<Folder>\n')
f.write('<Style id="icon_upc">\n')			
f.write('<IconStyle>\n')			
f.write('<Icon>\n')			
f.write('<href>threat.png</href>\n')			
f.write('	</Icon>\n')			
f.write('</IconStyle>\n')			
f.write('</Style>\n')			
f.write('<Placemark>\n')	
f.write('<name> Threat,')
f.write(latitude)
f.write(', ')
f.write(longitude)
f.write('</name>\n')
f.write('<styleUrl>#icon_upc</styleUrl>\n')
f.write('<description></description>\n')        
f.write('<Point>\n')
f.write('<altitudeMode>clampToGround</altitudeMode>\n')	
f.write('<coordinates>')
f.write(longitude)
f.write(',')
f.write(latitude)  	
f.write('</coordinates>\n')   			
f.write('</Point>\n')   
f.write('</Placemark>\n')   
f.write('</Folder>\n')   
f.write('	</kml>\n')   	
f.close()
