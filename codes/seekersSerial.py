#SeekersSerial.py
# Code that reads from serial data and appends the data in format "hh:mm:ss,XX.XXXX,YY.YYYY,hhhh,RSSI" on three CSV (seeker_blue_hist.csv, )
# seeker_red_hist.csv, seeker_green_hist.csv; depending on the input. Input is expected to be "SX,hh:mm:ss,XX.XXXX,YY.YYYY,hhhh,RSSI"; where SX
# is the drone codename

import serial
import string
import csv
import re

ser = serial.Serial(
    port='COM3',\
    baudrate=115200,\
    parity=serial.PARITY_NONE,\
  # stopbits=serial.STOPBITS_ONE,\
   # bytesize=serial.EIGHTBITS,\
        timeout=2)

print("connected to: " + ser.portstr)

while True:
    line = ser.readline()
    line = line.decode()
    datablocks = re.split(',+', line)
    count = len(datablocks)
    if count > 1:
       seeker =  datablocks[0]
       time   =  datablocks[1]
       lat    =  datablocks[2]
       lon    =  datablocks[3]
       alt    =  datablocks[4]
       rssi   =  datablocks[5]
       rssi   = rssi.rstrip("\r\n")
       
       if seeker == 'SB':
        print(seeker,time)
        fd = open('seeker_blue_hist.csv','a')
        fd.write(time)
        fd.write(',')
        fd.write(lat)
        fd.write(',')
        fd.write(lon)
        fd.write(',')
        fd.write(alt)
        fd.write(',')
        fd.write(rssi)
        fd.write('\n')
        fd.close()
       if seeker == 'SG':
        print(seeker,time)
        fd = open('seeker_green_hist.csv','a')
        fd.write(time)
        fd.write(',')
        fd.write(lat)
        fd.write(',')
        fd.write(lon)
        fd.write(',')
        fd.write(alt)
        fd.write(',')
        fd.write(rssi)
        fd.write('\n')
        fd.close()    
       if seeker == 'SR':
        print(seeker,time)
        fd = open('seeker_red_hist.csv','a')
        fd.write(time)
        fd.write(',')
        fd.write(lat)
        fd.write(',')
        fd.write(lon)
        fd.write(',')
        fd.write(alt)
        fd.write(',')
        fd.write(rssi)
        fd.write('\n')
        fd.close()
ser.close()