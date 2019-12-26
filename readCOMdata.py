#!/usr/bin/python
import serial
import csv
import time

#file = raw_input('Save File As: ')
#saveFile = open(file, 'w')
saveFile = open('tempData_meterX.csv', 'w')

#serialport = raw_input('Enter Port: ')
port1 = '/dev/ttyUSB0';

print "MeterX detected"
print "Connecting to MeterX....", port1

meterX = serial.Serial(port1, 115200)

meterX.write('a')

print "Connected to MeterX"

i=0
n=0
st="";
saveFile.write("Time,Temperature");
saveFile.write("\n");

while i < 8: 
    #time.sleep(5)
    data = meterX.readline()
    #data = meterX.read(10)
    st= str(i*10) + "," + data;
    #saveFile.write(i*10,",",data)
    saveFile.write(st)
    #print data
    i=i+1

print "Data Transfer Complete"
