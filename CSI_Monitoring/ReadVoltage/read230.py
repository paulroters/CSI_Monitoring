from __future__ import absolute_import, division, print_function, \
                                                    unicode_literals
import time
import datetime
import serial
import os

FILE_NAME = "csiv2"

try:
    from ADCPi import ADCPi
except ImportError:
    print("Failed to import ADCPi from python system path")
    print("Importing from parent folder instead")
    try:
        import sys
        sys.path.append('..')
        from ADCPi import ADCPi
    except ImportError:
        raise ImportError(
            "Failed to import library from parent folder")
    



    
def readcurrent(channel):
    adc = ADCPi(0x6A, 0x6B, 12)
    
    curr = [0,0,0,0,0,0,0,0,0,0]
        
    curr[0] = ((adc.read_voltage(channel)-2.5994)*5.25323)
        #time.sleep(0.01)
    curr[1] = ((adc.read_voltage(channel)-2.5994)*5.25323)
        #time.sleep(0.01)
    curr[2] = ((adc.read_voltage(channel)-2.5994)*5.25323)
        #time.sleep(0.01)
    curr[3] = ((adc.read_voltage(channel)-2.5994)*5.25323)
        #time.sleep(0.01)
    curr[4] = ((adc.read_voltage(channel)-2.5994)*5.25323)
        #time.sleep(0.01)
    curr[5] = ((adc.read_voltage(channel)-2.5994)*5.25323)
        #time.sleep(0.01)
    curr[6] = ((adc.read_voltage(channel)-2.5994)*5.25323)
        #time.sleep(0.01)
    curr[7] = ((adc.read_voltage(channel)-2.5994)*5.25323)
        #time.sleep(0.01)
    curr[8] = ((adc.read_voltage(channel)-2.5994)*5.25323)
        #time.sleep(0.01)
    curr[9] = ((adc.read_voltage(channel)-2.5994)*5.25323)
        #time.sleep(0.01)
    
    
    output = (curr[0] + curr[1] + curr[2] + curr[3] + curr[4] + curr[5] + curr[6] + curr[7] + curr[8] + curr[9])/10
    output = "%.3f" % output
    channel = "%.0f" % channel
    return(output + "A")
    
 
def readvoltage(channel):
    adc = ADCPi(0x68, 0x69, 12)
    output = (adc.read_voltage(channel)*6.769)
    output = "%.3f" % output
    channel = "%.0f" % channel
    return(output + "V")

    
def readvoltage230():
    ##############
    ## Script listens to serial port and writes contents into a file
    ##############
    ## requires pySerial to be installed

    serial_port = '/dev/ttyS0';
    baud_rate = 9600; #In arduino, Serial.begin(baud_rate)
    ser = serial.Serial(serial_port, baud_rate)
    line = ser.readline()
    line = line.decode("utf-8") #ser.readline returns a binary, convert to string
    return line

def stringline():
    line = "  |  " + readvoltage(1) + "  |  " + readcurrent(1) + "  |  " + readvoltage(2) + "  |  " + readcurrent(2) + "  |  " + readvoltage(3) + "  |  " + readcurrent(3) + "  |  " + readvoltage(4) + "  |  " + readcurrent(4) + "  |  " + readvoltage(5) + "  |  " + readcurrent(5) + "  |  " + readvoltage230() + "  |  " + readcurrent(6)
    return line
            
    
def writetotxt(input, filename):
    with open(filename + ".txt" , "a+") as f:
        timestamp = datetime.datetime.now().strftime("[%m/%d/%y - %I:%M:%S]  :  ")
        f.write(timestamp)
        f.write(input)
    
    
def main():
    i = 10
    while True:
       # writetotxt(stringline(), FILE_NAME)
       # writetotxt('\n', FILE_NAME)
        writetotxt(readvoltage230(), 'testcsi')
        print(readvoltage230())
       # time.sleep(0.1) 
        
        if (i / 10 == 1):
            writetotxt('  |  Channel 1  |  Channel 1  |  Channel 1  |  Channel 1  |  Channel 1  |  Channel 1  |  Channel 1  |  Channel 1  |  Channel 1  |  Channel 1  |  Channel 1  |  \n', FILE_NAME)
            i = 0
        i += 1

if __name__ == "__main__":
    main()
