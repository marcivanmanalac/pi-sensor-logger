#!/usr/bin/env python3
#This is a generic script for logging sensor data from a sensor connected to a raspberry pi.
#To run this as a background process on the CLI, type 'python3 loggy.py &'
#type 'kill -9' followed by PID number to terminate process

#The script does the following.
#1)Creates a file for the sensor data for the pi
#2)Reads the incoming Serial data and writes it into a log file

#!/usr/bin/env python
import time
import serial
import datetime
from os.path import exists

########Naming and creating file for Sensor Log################
dt =  str(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
filename = 'SENSOR_SAMPLE' + dt +'.txt'
f = open('~/sensor_logs' + filename , 'w')

# Set Up Serial Port for the sensor
# Ensure you are using the correct header name in '/dev' which the component is plugged in to. 
# If the ETHUSB Hub Hat is attached, the ttyUSB number sometimes changes between zero and one.
# Ensure you are using the proper arguments for the device attached device
ser = serial.Serial(
        '/dev/ttyUSB0',
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

# Te program will continue to write into the file until it is terminated.
while 1:
    #Read the number of bytes coming in.
    data = ser.read(100)
    #Print debugger
    print(data)
    # Write into logger
    f.write(data)
    
f.close()
    
