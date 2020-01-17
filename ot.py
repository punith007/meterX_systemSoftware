#!/usr/bin/python
import serial
import csv
import time
import os


from tkinter import * 
from tkinter import ttk 
  
# import only asksaveasfile from filedialog 
# which is used to save file in any extension 
from tkinter.filedialog import asksaveasfile 

saveFile = open('tempData_meterX.csv', 'w')

#serialport = raw_input('Enter Port: ')
port1 = '/dev/ttyUSB0';

print "MeterX detected"
print "Connecting to MeterX....", port1

meterX = serial.Serial(port1, 115200)
tempfile=""

#writing to the file
saveFile.write("Time,Temperature");
saveFile.write("\n");
##########

root = Tk() 
#root.geometry('200x150') 
root.geometry('600x400') 
  
# function to call when user press 
# the save button, a filedialog will 
# open and ask to save file 
def save(): 
    files = [('All Files', '*.*'),  
             ('Python Files', '*.py'), 
             ('csv Files', '*.csv'), 
             ('Text Document', '*.txt')] 
    file = asksaveasfile(filetypes = files, defaultextension = files)
    print file.name

    command = "cp " + "tempData_meterX.csv "+ file.name 
    print command
    os.system(command)


    label = Label(root, anchor = W, text= "File saved at"+file.name)
    label.pack()

def extract():
    i=0
    n=0
    st=""
    print 'Extracting Data'

    meterX.write('a')
    print "Connected to MeterX"

    ############################
    while i < 8:
        data = meterX.readline()
        st= str(i*10) + "," + data;
        saveFile.write(st)
        i=i+1

    saveFile.close()
    ##########################
    print "Data Transfer Complete"

    label = Label(root, anchor = W, text= "Data Transfer Completed ")
    label.pack()

#############################################################
#btn = ttk.Button(root, text = 'Save', command = lambda : save()) 
btn = ttk.Button(root, text = 'Save', command = save) 
#btn1 = ttk.Button(root, text = 'Extr', command = lambda : extract()) 
btn1 = ttk.Button(root, text = 'Extr', command =  extract) 
btn1.pack(side = TOP, padx = 50, pady = 10) 
btn.pack(side = TOP, padx = 60, pady = 10) 
#btn1.pack(side = LEFT) 
#btn.pack(side = LEFT) 
  
mainloop() 
