## Code that get the last points form the three 3 CSV for the position of each drone, the 10 last points from the CSV to average the RSSI 
## and creates KMLs 
## It creates the KMLs with the radios based on the first and third percentil

import csv
import pandas as pd
import simplekml
from polycircles import polycircles
import numpy as np

last_points = 5 #last points to read to calculate mean and percentils of RSSI
rssitrans_quad = 0.03573 #Quadratic coefficient of the f(RSSI) = Distance. It follows a model like: Distance = coefquad·RSSI^2 + coeflin·RSSI + zero
rssitrans_lin  = 5.294   #Linear coefficient
rssitrans_off  = 192.9   #Offset coeficient
vertices = 36 #  Circles vertices. 36 is good 
transparency = 100 #0 to 200

#Blue Seeker
data_initial = open("seeker_blue_hist.csv", "r")
data = csv.reader((line.replace('\0','') for line in data_initial), delimiter=",")
df = pd.DataFrame(data)
df.columns = ['time', 'lat','long','alt','rssi']
df1 = df.tail(last_points)
df1[["rssi"]] = df1[["rssi"]].apply(pd.to_numeric)
first_quartile = np.percentile(df1.rssi, 25)
third_quartile = np.percentile(df1.rssi, 75)
df2 = df.tail(1)
time = df2.time.values[0]
latitude = float(df2.lat.values[0])
longitude = float(df2.long.values[0])
altitude = float(df2.alt.values[0])
rssimean = str(df1["rssi"].mean())
rssimean = round(float(rssimean), 5)
radius = abs(rssitrans_quad*rssimean*rssimean+rssitrans_lin*rssimean+rssitrans_off)

radius_outer = abs(rssitrans_quad*first_quartile*first_quartile+rssitrans_lin*first_quartile+rssitrans_off)
radius_inner = abs(rssitrans_quad*third_quartile*third_quartile+rssitrans_lin*third_quartile+rssitrans_off)

outer_polycircle = polycircles.Polycircle(latitude=latitude,
                                    longitude=longitude,
                                    radius=radius_outer,
                                    number_of_vertices=vertices)
inner_polycircle = polycircles.Polycircle(latitude=latitude,
                                    longitude=longitude,
                                    radius=radius_inner,
                                    number_of_vertices=vertices)


kml = simplekml.Kml()
pol = kml.newpolygon(name="Blue Torus",
                                         outerboundaryis=outer_polycircle.to_kml(),
                                         innerboundaryis=inner_polycircle.to_kml())
pol.style.polystyle.color = \
        simplekml.Color.changealphaint(transparency, simplekml.Color.blue)
kml.save("blueTorus.kml")



#Red Seeker
data_initial = open("seeker_red_hist.csv", "r")
data = csv.reader((line.replace('\0','') for line in data_initial), delimiter=",")
df = pd.DataFrame(data)
df.columns = ['time', 'lat','long','alt','rssi']
df1 = df.tail(last_points)
df1[["rssi"]] = df1[["rssi"]].apply(pd.to_numeric)
first_quartile = np.percentile(df1.rssi, 25)
third_quartile = np.percentile(df1.rssi, 75)
df2 = df.tail(1)
time = df2.time.values[0]
latitude = float(df2.lat.values[0])
longitude = float(df2.long.values[0])
altitude = float(df2.alt.values[0])
rssimean = str(df1["rssi"].mean())
rssimean = round(float(rssimean), 5)
radius = abs(rssitrans_quad*rssimean*rssimean+rssitrans_lin*rssimean+rssitrans_off)

radius_outer = abs(rssitrans_quad*first_quartile*first_quartile+rssitrans_lin*first_quartile+rssitrans_off)
radius_inner = abs(rssitrans_quad*third_quartile*third_quartile+rssitrans_lin*third_quartile+rssitrans_off)

outer_polycircle = polycircles.Polycircle(latitude=latitude,
                                    longitude=longitude,
                                    radius=radius_outer,
                                    number_of_vertices=vertices)
inner_polycircle = polycircles.Polycircle(latitude=latitude,
                                    longitude=longitude,
                                    radius=radius_inner,
                                    number_of_vertices=vertices)


kml = simplekml.Kml()
pol = kml.newpolygon(name="Red Torus",
                                         outerboundaryis=outer_polycircle.to_kml(),
                                         innerboundaryis=inner_polycircle.to_kml())
pol.style.polystyle.color = \
        simplekml.Color.changealphaint(transparency, simplekml.Color.red)
kml.save("redTorus.kml")


#Green Seeker
data_initial = open("seeker_green_hist.csv", "r")
data = csv.reader((line.replace('\0','') for line in data_initial), delimiter=",")
df = pd.DataFrame(data)
df.columns = ['time', 'lat','long','alt','rssi']
df1 = df.tail(last_points)
df1[["rssi"]] = df1[["rssi"]].apply(pd.to_numeric)
first_quartile = np.percentile(df1.rssi, 25)
third_quartile = np.percentile(df1.rssi, 75)
df2 = df.tail(1)
time = df2.time.values[0]
latitude = float(df2.lat.values[0])
longitude = float(df2.long.values[0])
altitude = float(df2.alt.values[0])
rssimean = str(df1["rssi"].mean())
rssimean = round(float(rssimean), 5)
radius = abs(rssitrans_quad*rssimean*rssimean+rssitrans_lin*rssimean+rssitrans_off)

radius_outer = abs(rssitrans_quad*first_quartile*first_quartile+rssitrans_lin*first_quartile+rssitrans_off)
radius_inner = abs(rssitrans_quad*third_quartile*third_quartile+rssitrans_lin*third_quartile+rssitrans_off)

outer_polycircle = polycircles.Polycircle(latitude=latitude,
                                    longitude=longitude,
                                    radius=radius_outer,
                                    number_of_vertices=vertices)
inner_polycircle = polycircles.Polycircle(latitude=latitude,
                                    longitude=longitude,
                                    radius=radius_inner,
                                    number_of_vertices=vertices)


kml = simplekml.Kml()
pol = kml.newpolygon(name="Green Torus",
                                         outerboundaryis=outer_polycircle.to_kml(),
                                         innerboundaryis=inner_polycircle.to_kml())
pol.style.polystyle.color = \
        simplekml.Color.changealphaint(transparency, simplekml.Color.green)
kml.save("greenTorus.kml")