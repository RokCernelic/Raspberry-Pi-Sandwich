#!/usr/bin/env python
# UL PeF, Rok Cernelic, 2014
from RoPi_lib import *


# ===========================================================================
# PORTB (DIGITAL INPUT, OUTPUT)
# ===========================================================================
'''
PORTB.setup(pin, PORTB.IN)      # Ignore. Allerady set in the library for pins 0-7
PORTB.pullup(pin, 1)            # Ignore. Allerady set in the library for pins 0-7
PORTB.input(pin)                # Call input pin 0-7

PORTB.setup(pin, PORTB.OUT)     # Set pin as output (overrides library setup)
PORTB.output(pin, value)        # Set output pin 0-7 as High/Low
'''

# Example 2
# Checking buttons 0-7
while True:
    if PORTB.input(7) == 0:
        print "7"
    if PORTB.input(6) == 0:
        print "6"
    if PORTB.input(5) == 0:
        print "5"
    if PORTB.input(4) == 0:
        print "4"
    if PORTB.input(3) == 0:
        print "3"
    if PORTB.input(2) == 0:
        print "2"
    if PORTB.input(1) == 0:
        print "1"
    if PORTB.input(0) == 0:
        print "0"
