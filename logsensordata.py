#!/usr/bin/env python

"""
wirtes one logfile for sensor current and voltage
"""
import logging
import ADCPi

def main():
    '''
    Main program function
    '''

    adc1 = ADCPi(0x68, 0x69, 12)         #i2c address ADC 1
    adc2 = ADCPi()                       #i2c address ADC 2
    adc3 = ADCPi()                       #i2c address ADC 3

    logging.basicConfig(filename='sensordata', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    logging.basicConfig(level=logging.INFO)

    while True:  
        logging.info('Voltage Channel 1: %02f\n' % (adc1.read_voltage(1)*5)) )
        # other ports


        # wait 1 second before reading the pins again
        time.sleep(1)

if __name__ == "__main__":
    main()