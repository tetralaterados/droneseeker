import csv
import pandas as pd


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



#Values Blue. Mid-Point is considered to be attached in ground (No altitude)
latitudeBlue = dfBlue.lat.values[0]
longitudeBlue = dfBlue.long.values[0]

#Values Red. Mid-Point is considered to be attached in ground (No altitude)
latitudeRed = dfRed.lat.values[0]
longitudeRed = dfRed.long.values[0]

#Values Green. Mid-Point is considered to be attached in ground (No altitude)
latitudeGreen = dfGreen.lat.values[0]
longitudeGreen = dfGreen.long.values[0]

#Convert to float
latitudeBlue = float(latitudeBlue)
longitudeBlue = float(longitudeBlue)

latitudeRed = float(latitudeRed)
longitudeRed = float(longitudeRed)

latitudeGreen = float(latitudeGreen)
longitudeGreen = float(longitudeGreen)

#Calculating mean
latmean = (latitudeGreen + latitudeBlue + latitudeRed)/3
lonmean = (longitudeGreen + longitudeBlue + longitudeRed)/3

#Getting time
timeBlue = dfBlue.time.values[0]
timeGreen = dfGreen.time.values[0]
timeRed = dfRed.time.values[0]

fd = open('midpointHist.csv','a')
fd.write(str(latmean))
fd.write(',')
fd.write(str(lonmean))
fd.write(',')
fd.write(str(timeBlue))
fd.write(',')
fd.write(str(timeGreen))
fd.write(',')
fd.write(str(timeRed))
fd.write('\n')
fd.close()