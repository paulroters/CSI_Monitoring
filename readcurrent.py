#!/usr/bin/env python



"""
Initialise the ADC device using the default addresses and sample rate, change
this value if you have changed the address selection jumpers
Sample rate can be 12,14, 16 or 18
"""

from __future__ import absolute_import, division, print_function, \
                                                    unicode_literals
import time
import datetime

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


def writetofile(texttowrtite):
    '''
    Open the log file, write the value and close the file.
    '''
    file = open('adclog.txt', 'a')
    file.write(str(datetime.datetime.now()) + " " + texttowrtite)
    file.close()


def main():
    '''
    Main program function
    '''

    adc = ADCPi(0x68, 0x69, 12)

    print("Logging...")

    offset = float(0.0)

    while True:

        # read from adc channels and write to the log file
        writetofile("Channel 1: %02f\n" % ((adc.read_voltage(1)-offset)*0.185))
        writetofile("Channel 2: %02f\n" % ((adc.read_voltage(2)-offset)*0.185))
        writetofile("Channel 3: %02f\n" % ((adc.read_voltage(3)-offset)*0.185))
        writetofile("Channel 4: %02f\n" % ((adc.read_voltage(4)-offset)*0.185))
        writetofile("Channel 5: %02f\n" % ((adc.read_voltage(5)-offset)*0.185))
        writetofile("Channel 6: %02f\n" % ((adc.read_voltage(6)-offset)*0.185))
        writetofile("Channel 7: %02f\n" % ((adc.read_voltage(7)-offset)*0.185))
        writetofile("Channel 8: %02f\n" % ((adc.read_voltage(8)-offset)*0.185))

        # wait 1 second before reading the pins again
        time.sleep(1)

if __name__ == "__main__":
    main()