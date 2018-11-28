#!/usr/bin/env python
"""
================================================
ABElectronics ADC Pi 8-Channel ADC demo

Requires python smbus to be installed
run with: python demo_readvoltage.py
================================================

Initialise the ADC device using the default addresses and sample rate,
change this value if you have changed the address selection jumpers

Sample rate can be 12,14, 16 or 18
"""

from __future__ import absolute_import, division, print_function, \
                                                    unicode_literals
import time
import os

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


def main():
    '''
    Main program function
    '''

    adc = ADCPi(0x6A, 0x6B, 12)

    while True:
        
        curr = [0,0,0,0,0,0,0,0,0,0]
        curr[0] = ((adc.read_voltage(5)-2.5994)*5.25323)
        #time.sleep(0.01)
        curr[1] = ((adc.read_voltage(5)-2.5994)*5.25323)
        #time.sleep(0.01)
        curr[2] = ((adc.read_voltage(5)-2.5994)*5.25323)
        #time.sleep(0.01)
        curr[3] = ((adc.read_voltage(5)-2.5994)*5.25323)
        #time.sleep(0.01)
        curr[4] = ((adc.read_voltage(5)-2.5994)*5.25323)
        #time.sleep(0.01)
        curr[5] = ((adc.read_voltage(5)-2.5994)*5.25323)
        #time.sleep(0.01)
        curr[6] = ((adc.read_voltage(5)-2.5994)*5.25323)
        #time.sleep(0.01)
        curr[7] = ((adc.read_voltage(5)-2.5994)*5.25323)
        #time.sleep(0.01)
        curr[8] = ((adc.read_voltage(5)-2.5994)*5.25323)
        #time.sleep(0.01)
        curr[9] = ((adc.read_voltage(5)-2.5994)*5.25323)
        #time.sleep(0.01)
    
    
        output = (curr[0] + curr[1] + curr[2] + curr[3] + curr[4] + curr[5] + curr[6] + curr[7] + curr[8] + curr[9])/10

        print("I2C 0x6A Channel 6: %02f" % output)
        


        # wait 0.2 seconds before reading the pins again
        time.sleep(0.2)

if __name__ == "__main__":
    main()
