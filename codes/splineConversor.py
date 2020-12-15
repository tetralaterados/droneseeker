#splineConversor.py
# Code that reads a configurable number of points from 3 CSV:
# INPUTS: (seeker_blue_hist.csv,seeker_red_hist.csv, seeker_green_hist.csv) 
# and creates the corresponding KML Spline:
# OUTPUTS splineBlue.kml, splineGreen.kml, splineRed.kml. 


import csv
import pandas as pd


last_points = 15



#Blue Spline
data_initial = open("seeker_blue_hist.csv", "r")
data = csv.reader((line.replace('\0','') for line in data_initial), delimiter=",")
df = pd.DataFrame(data)
df.columns = ['time', 'lat','long','alt','rssi']
df = df.tail(last_points)

f = open('splineBlue.kml', 'w')

f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
f.write("	<Document>\n")
f.write("	<name>Blue Drone Path</name>\n")
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
f.write("			<name> Blue Drone Path </name>\n")
f.write("			<styleUrl>#style1</styleUrl> \n")
f.write("   		<LineString>\n")
f.write("   		<extrude>1</extrude>\n")
f.write("   		<tessellate>1</tessellate>\n")
f.write("   		<altitudeMode>absolute</altitudeMode>\n")
f.write("			<coordinates>")
for index, row in df.iterrows():
  	f.write("			"+row['long']+","+row['lat']+","+row['alt']+"\n")
f.write("			</coordinates>\n")
f.write("			</LineString>\n")
f.write("		</Placemark>\n")
f.write("</Document>")
f.write("</kml>")
f.close()



#Green Spline

data_initial = open("seeker_green_hist.csv", "r")
data = csv.reader((line.replace('\0','') for line in data_initial), delimiter=",")
df = pd.DataFrame(data)
df.columns = ['time', 'lat','long','alt','rssi']
df = df.tail(last_points)
f = open('splineGreen.kml', 'w')


f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
f.write("	<Document>\n")
f.write("	<name>Green Drone Path</name>\n")
f.write('	<Style id="style1">\n')
f.write("		<LineStyle>\n")
f.write("			<color>6414F000</color>\n")
f.write("			<width>4</width>\n")
f.write("		</LineStyle>\n")
f.write("		<PolyStyle>\n")
f.write("			<color>1414F000</color>\n")
f.write("		</PolyStyle>\n")
f.write("	</Style>\n")
f.write("		<Placemark>\n")
f.write("			<name> Green Drone Path </name>\n")
f.write("			<styleUrl>#style1</styleUrl> \n")
f.write("   		<LineString>\n")
f.write("   		<extrude>1</extrude>\n")
f.write("   		<tessellate>1</tessellate>\n")
f.write("   		<altitudeMode>absolute</altitudeMode>\n")
f.write("			<coordinates>")
for index, row in df.iterrows():
      	f.write("			"+row['long']+","+row['lat']+","+row['alt']+"\n")
f.write("			</coordinates>\n")
f.write("			</LineString>\n")
f.write("		</Placemark>\n")
f.write("</Document>")
f.write("</kml>")
f.close()



#Red Spline
data_initial = open("seeker_red_hist.csv", "r")
data = csv.reader((line.replace('\0','') for line in data_initial), delimiter=",")
df = pd.DataFrame(data)
df.columns = ['time', 'lat','long','alt','rssi']
df = df.tail(last_points)



f = open('splineRed.kml', 'w')

f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
f.write("	<Document>\n")
f.write("	<name>Red Drone Path</name>\n")
f.write('	<Style id="style1">\n')
f.write("		<LineStyle>\n")
f.write("			<color>641400F0</color>\n")
f.write("			<width>4</width>\n")
f.write("		</LineStyle>\n")
f.write("		<PolyStyle>\n")
f.write("			<color>f1400F0</color>\n")
f.write("		</PolyStyle>\n")
f.write("	</Style>\n")
f.write("		<Placemark>\n")
f.write("			<name> Red Drone Path </name>\n")
f.write("			<styleUrl>#style1</styleUrl> \n")
f.write("   		<LineString>\n")
f.write("   		<extrude>1</extrude>\n")
f.write("   		<tessellate>1</tessellate>\n")
f.write("   		<altitudeMode>absolute</altitudeMode>\n")
f.write("			<coordinates>")
for index, row in df.iterrows():
      	f.write("			"+row['long']+","+row['lat']+","+row['alt']+"\n")
f.write("			</coordinates>\n")
f.write("			</LineString>\n")
f.write("		</Placemark>\n")
f.write("</Document>")
f.write("</kml>")
f.close()
