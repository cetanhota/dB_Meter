#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 13:41:50 2018

@author: wayne
"""

import serial # import Serial Library
import numpy  # Import numpy
import matplotlib.pyplot as plt #import matplotlib library
from drawnow import *

dB= []

arduinoData = serial.Serial('/dev/cu.usbmodem141401', 115200) #Creating our serial object named arduinoData
plt.ion() #Tell matplotlib you want interactive mode to plot live data
cnt=0

def makeFig(): 					 #Create a function that makes our desired plot
    #plt.ylim(50,68)                             #Set y min and max values
    plt.title('Sound Level Meter')         	#Plot the title
    plt.grid(True)                              #Turn the grid on
    plt.ylabel('Decibel')                       #Set ylabels
    plt.plot(dB, 'b.-', label='dB Level')       #plot the temperature
    plt.legend(loc='upper left')                #plot the legend


while True:
    while (arduinoData.inWaiting()==0):
        pass
    arduinoString = arduinoData.readline()
    dataArray = arduinoString.split(',')
    tempdB = float( dataArray[0] )
    dB.append(tempdB)
    drawnow(makeFig)
    plt.pause(.000001)
    cnt=cnt+1
    if(cnt>50):
        dB.pop(0)
