#!/usr/bin/python

# Copyright (C) 2007 by Jaroslaw Zachwieja <grok!warwick.ac.uk>
# Copyright (C) 2008 by TJ <linux!tjworld.net>
# Published under the terms of GNU General Public License v2 or later.
# License text available at http://www.gnu.org/licenses/licenses.html#GPL

import serial
import string
import sys
import getopt
import csv

def usage():
		print "Usage:"
		print " -p | --port <device>   e.g. /dev/ttyS0"
		print " -b | --baud <speed>    e.g. 4800"
		print " -f | --file <filename> e.g. /tmp/gps.kml"
		print " -h | --help     display options"

def main():
	# defaults
	serial_port = "/dev/ttyUSB0"
	serial_baud = 115200
	file = './gpsballoon.kml'
	csv_balloon = './csv_balloon.csv'

	try:
		opts, args = getopt.getopt(sys.argv[1:], "p:b:f:h", ["port=", "baud=", "file=", "help"])
	except getopt.GetoptError:
		usage()
		sys.exit(1)
	else:
		for opt, arg in opts:
			if opt in ("-p", "--port"):
				serial_port = arg
			elif opt in ("-b", "--baud"):
				serial_baud = string.atof(arg)
			elif opt in ("-f", "--file"):
				file = arg
			elif opt in ("-h", "--help"):
				usage()
				sys.exit(0)
			else:
				print "Unknown option"

	gps = serial.Serial(serial_port, serial_baud, timeout=1)

	print "Serving data from %s (%d baud) to %s" % (serial_port, serial_baud, file)

	latitude = 0
	longitude = 0
	speed = 0
	heading_in = 0
	altitude = 0
	while 1:
		line = gps.readline()
		datablock = line.split(',') 

		
		time = datablock[0]
		longitude = string.atof(datablock[2])
		latitude = string.atof(datablock[1])
		altitude = string.atof(datablock[3])
		fd = open('gps_balloon.csv','a')
		print time, latitude, longitude, altitude
		fd.write(str(time))
		fd.write(',')
		fd.write(str(latitude))
		fd.write(',')
		fd.write(str(longitude))
		fd.write(',')
		fd.write(str(altitude))
		fd.write('\n')
		fd.close()

		output = """<?xml version="1.0" encoding="UTF-8"?>
					<kml xmlns="http://earth.google.com/kml/2.0">
					<Folder>
					<Style id="icon_upc">
    				<IconStyle>
       				<Icon>
       			    <href>icon_upc.png</href>
        			</Icon>
    				</IconStyle>
					</Style>
					<Placemark>
					<name> Balloon %s,%s, %s, %s </name>
					<styleUrl>#icon_upc</styleUrl>
					<description></description>
					<Point>
					<altitudeMode>absolute</altitudeMode>
					<coordinates>%s,%s,%s</coordinates>
					</Point>
					</Placemark>
					</Folder>
					</kml>""" % (time, latitude, longitude,altitude,longitude,latitude,altitude)
		f=open(file, 'w')
		f.write(output)
		f.close()


	ser.close()







if __name__ == "__main__":
	main()