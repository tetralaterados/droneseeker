#Triangle.py
# Code that reads the very lasts point of three 3 CSV:
# INPUTS: (seeker_blue_hist.csv,seeker_red_hist.csv, seeker_green_hist.csv) 
# and creates a KML spline (triangle) between three points
# OUTPUTS GreenRed.kml, RedBlue.kml, BlueRed.kml
# In the spline is included the distance among the three drones


import geopy.distance
import csv
import pandas as pd

######################## Data Treatment

############ Data adquisition

#Blue Seeker
data_initial = open("seeker_blue_hist.csv", "r")
data = csv.reader((line.replace('\0','') for line in data_initial), delimiter=",")
dfBlue = pd.DataFrame(data)
dfBlue.columns = ['time', 'lat','long','alt','rssi']
dfBlue = dfBlue.tail(1)

#Red Seeker
data_initial = open("seeker_red_hist.csv", "r")
data = csv.reader((line.replace('\0','') for line in data_initial), delimiter=",")
dfRed = pd.DataFrame(data)
dfRed.columns = ['time', 'lat','long','alt','rssi']
dfRed = dfRed.tail(1)

#Green Seeker
data_initial = open("seeker_green_hist.csv", "r")
data = csv.reader((line.replace('\0','') for line in data_initial), delimiter=",")
dfGreen = pd.DataFrame(data)
dfGreen.columns = ['time', 'lat','long','alt','rssi']
dfGreen = dfGreen.tail(1)

#MidPoint
data_initial = open("midpointHist.csv", "r")
data = csv.reader((line.replace('\0','') for line in data_initial), delimiter=",")
dfMid = pd.DataFrame(data)
dfMid .columns = ['latmean', 'longmean','timeBlue','TimeGreen','TimeRead']
dfMid  = dfMid .tail(1)

############ Values adquisition

#Values Blue. Mid-Point is considered to be attached in ground (No altitude)
latitudeBlue = dfBlue.lat.values[0]
longitudeBlue = dfBlue.long.values[0]

#Values Red. Mid-Point is considered to be attached in ground (No altitude)
latitudeRed = dfRed.lat.values[0]
longitudeRed = dfRed.long.values[0]

#Values Green. Mid-Point is considered to be attached in ground (No altitude)
latitudeGreen = dfGreen.lat.values[0]
longitudeGreen = dfGreen.long.values[0]

#Values Mid. Mid-Point is considered to be attached in ground (No altitude)
latitudeMid = dfMid.latmean.values[0]
longitudeMid = dfMid.longmean.values[0]



############ Format convert

#Convert to float
latitudeBlue = float(latitudeBlue)
longitudeBlue = float(longitudeBlue)

latitudeRed = float(latitudeRed)
longitudeRed = float(longitudeRed)

latitudeGreen = float(latitudeGreen)
longitudeGreen = float(longitudeGreen)

latitudeMid = float(latitudeMid)
longitudeMid = float(longitudeMid)


############ Convert to Coordinates
coordsGreen = (latitudeGreen,longitudeGreen);
coordsRed   = (latitudeRed,longitudeRed);
coordsBlue  = (latitudeBlue,longitudeBlue);
coordsMid   = (latitudeMid, longitudeMid);

############ Distance Calculation
distGreenRed = geopy.distance.geodesic(coordsGreen, coordsRed).m
distRedBlue = geopy.distance.geodesic(coordsRed, coordsBlue).m
distBlueGreen = geopy.distance.geodesic(coordsBlue, coordsGreen).m

distGreenMid = geopy.distance.geodesic(coordsMid, coordsGreen).m
distBlueMid = geopy.distance.geodesic(coordsMid, coordsBlue).m
distRedMid = geopy.distance.geodesic(coordsMid, coordsRed).m

distGreenRed = round(float(distGreenRed), 0)
distGreenRed = str(distGreenRed)

distRedBlue = round(float(distRedBlue), 0)
distRedBlue = str(distRedBlue)

distBlueGreen = round(float(distBlueGreen), 0)
distBlueGreen = str(distBlueGreen)

distBlueGreen = round(float(distBlueGreen), 0)
distBlueGreen = str(distBlueGreen)

## To Mid

distBlueMid = round(float(distBlueMid), 0)
distBlueMid = str(distBlueMid)

distGreenMid = round(float(distGreenMid), 0)
distGreenMid = str(distGreenMid)

distRedMid = round(float(distRedMid), 0)
distRedMid = str(distRedMid)


######################## Distance Calculation

#Green Red
f = open('GreenRed.kml', 'w')
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
f.write("	<Document>\n")
f.write("	<name>Green-Red Distance</name>\n")
f.write('	<Style id="style1">\n')
f.write("		<LineStyle>\n")
f.write("			<color>64000014</color>\n")
f.write("			<width>4</width>\n")
f.write("		</LineStyle>\n")
f.write("		<PolyStyle>\n")
f.write("			<color>64000014</color>\n")
f.write("		</PolyStyle>\n")
f.write("	</Style>\n")
f.write("		<Placemark>\n")
f.write("			<name> Green-Red Distance = ")
f.write(distGreenRed)
f.write("</name>\n")
f.write("			<styleUrl>#style1</styleUrl> \n")
f.write("   		<LineString>\n")
f.write("   		<extrude>1</extrude>\n")
f.write("   		<tessellate>1</tessellate>\n")
f.write("   		<altitudeMode>distGreenRed</altitudeMode>\n")
f.write("			<coordinates>")
f.write(str(longitudeGreen))
f.write(",")
f.write(str(latitudeGreen))
f.write("\n")
f.write(str(longitudeRed))
f.write(",")
f.write(str(latitudeRed))
f.write("			</coordinates>\n")
f.write("			</LineString>\n")
f.write("		</Placemark>\n")
f.write("</Document>")
f.write("</kml>")
f.close()



#Blue Red
f = open('BlueRed.kml', 'w')
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
f.write("	<Document>\n")
f.write("	<name>Blue-Red Distance</name>\n")
f.write('	<Style id="style1">\n')
f.write("		<LineStyle>\n")
f.write("			<color>64000014</color>\n")
f.write("			<width>4</width>\n")
f.write("		</LineStyle>\n")
f.write("		<PolyStyle>\n")
f.write("			<color>64000014</color>\n")
f.write("		</PolyStyle>\n")
f.write("	</Style>\n")
f.write("		<Placemark>\n")
f.write("			<name> Blue-Red Distance = ")
f.write(str(distRedBlue))
f.write("</name>\n")
f.write("			<styleUrl>#style1</styleUrl> \n")
f.write("   		<LineString>\n")
f.write("   		<extrude>1</extrude>\n")
f.write("   		<tessellate>1</tessellate>\n")
f.write("   		<altitudeMode>distGreenRed</altitudeMode>\n")
f.write("			<coordinates>")
f.write(str(longitudeBlue))
f.write(",")
f.write(str(latitudeBlue))
f.write("\n")
f.write(str(longitudeRed))
f.write(",")
f.write(str(latitudeRed))
f.write("			</coordinates>\n")
f.write("			</LineString>\n")
f.write("		</Placemark>\n")
f.write("</Document>")
f.write("</kml>")
f.close()



#Blue Green
f = open('BlueGreen.kml', 'w')
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
f.write("	<Document>\n")
f.write("	<name>Blue-Green Distance</name>\n")
f.write('	<Style id="style1">\n')
f.write("		<LineStyle>\n")
f.write("			<color>64000014</color>\n")
f.write("			<width>4</width>\n")
f.write("		</LineStyle>\n")
f.write("		<PolyStyle>\n")
f.write("			<color>64000014</color>\n")
f.write("		</PolyStyle>\n")
f.write("	</Style>\n")
f.write("		<Placemark>\n")
f.write("			<name> Blue Green Distance = ")
f.write(str(distBlueGreen))
f.write("</name>\n")
f.write("			<styleUrl>#style1</styleUrl> \n")
f.write("   		<LineString>\n")
f.write("   		<extrude>1</extrude>\n")
f.write("   		<tessellate>1</tessellate>\n")
f.write("   		<altitudeMode>distGreenRed</altitudeMode>\n")
f.write("			<coordinates>")
f.write(str(longitudeBlue))
f.write(",")
f.write(str(latitudeBlue))
f.write("\n")
f.write(str(longitudeGreen))
f.write(",")
f.write(str(latitudeGreen))
f.write("			</coordinates>\n")
f.write("			</LineString>\n")
f.write("		</Placemark>\n")
f.write("</Document>")
f.write("</kml>")
f.close()



#Blue Mid
f = open('BlueMid.kml', 'w')
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
f.write("	<Document>\n")
f.write("	<name>Blue-Mid Distance</name>\n")
f.write('	<Style id="style1">\n')
f.write("		<LineStyle>\n")
f.write("			<color>64000014</color>\n")
f.write("			<width>4</width>\n")
f.write("		</LineStyle>\n")
f.write("		<PolyStyle>\n")
f.write("			<color>64000014</color>\n")
f.write("		</PolyStyle>\n")
f.write("	</Style>\n")
f.write("		<Placemark>\n")
f.write("			<name> Blue Mid Distance = ")
f.write(str(distBlueMid))
f.write("</name>\n")
f.write("			<styleUrl>#style1</styleUrl> \n")
f.write("   		<LineString>\n")
f.write("   		<extrude>1</extrude>\n")
f.write("   		<tessellate>1</tessellate>\n")
f.write("   		<altitudeMode>distGreenRed</altitudeMode>\n")
f.write("			<coordinates>")
f.write(str(longitudeBlue))
f.write(",")
f.write(str(latitudeBlue))
f.write("\n")
f.write(str(longitudeMid))
f.write(",")
f.write(str(latitudeMid))
f.write("			</coordinates>\n")
f.write("			</LineString>\n")
f.write("		</Placemark>\n")
f.write("</Document>")
f.write("</kml>")
f.close()


#Red Mid
f = open('RedMid.kml', 'w')
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
f.write("	<Document>\n")
f.write("	<name>Red-Mid Distance</name>\n")
f.write('	<Style id="style1">\n')
f.write("		<LineStyle>\n")
f.write("			<color>64000014</color>\n")
f.write("			<width>4</width>\n")
f.write("		</LineStyle>\n")
f.write("		<PolyStyle>\n")
f.write("			<color>64000014</color>\n")
f.write("		</PolyStyle>\n")
f.write("	</Style>\n")
f.write("		<Placemark>\n")
f.write("			<name> Red Mid Distance = ")
f.write(str(distRedMid))
f.write("</name>\n")
f.write("			<styleUrl>#style1</styleUrl> \n")
f.write("   		<LineString>\n")
f.write("   		<extrude>1</extrude>\n")
f.write("   		<tessellate>1</tessellate>\n")
f.write("   		<altitudeMode>distGreenRed</altitudeMode>\n")
f.write("			<coordinates>")
f.write(str(longitudeRed))
f.write(",")
f.write(str(latitudeRed))
f.write("\n")
f.write(str(longitudeMid))
f.write(",")
f.write(str(latitudeMid))
f.write("			</coordinates>\n")
f.write("			</LineString>\n")
f.write("		</Placemark>\n")
f.write("</Document>")
f.write("</kml>")
f.close()


#Green Mid
f = open('GreenMid.kml', 'w')
f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
f.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
f.write("	<Document>\n")
f.write("	<name>Green-Mid Distance</name>\n")
f.write('	<Style id="style1">\n')
f.write("		<LineStyle>\n")
f.write("			<color>64000014</color>\n")
f.write("			<width>4</width>\n")
f.write("		</LineStyle>\n")
f.write("		<PolyStyle>\n")
f.write("			<color>64000014</color>\n")
f.write("		</PolyStyle>\n")
f.write("	</Style>\n")
f.write("		<Placemark>\n")
f.write("			<name> Green Mid Distance = ")
f.write(str(distGreenMid))
f.write("</name>\n")
f.write("			<styleUrl>#style1</styleUrl> \n")
f.write("   		<LineString>\n")
f.write("   		<extrude>1</extrude>\n")
f.write("   		<tessellate>1</tessellate>\n")
f.write("   		<altitudeMode>distGreenRed</altitudeMode>\n")
f.write("			<coordinates>")
f.write(str(longitudeGreen))
f.write(",")
f.write(str(latitudeGreen))
f.write("\n")
f.write(str(longitudeMid))
f.write(",")
f.write(str(latitudeMid))
f.write("			</coordinates>\n")
f.write("			</LineString>\n")
f.write("		</Placemark>\n")
f.write("</Document>")
f.write("</kml>")
f.close()