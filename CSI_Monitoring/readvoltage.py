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


