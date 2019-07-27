#!/usr/bin/python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

# Set #18 as buzzer pin
BuzzerPin = 18

def setup():
    # Set the GPIO modes to BCM Numbering
    GPIO.setmode(GPIO.BCM)
    # Set BuzzerPin's mode to output,
    # and initial level to High(3.3v)
    GPIO.setup(BuzzerPin, GPIO.OUT, initial=GPIO.HIGH)

# main function
def main():
    while True:
    	GPIO.output(BuzzerPin, GPIO.LOW)
        time.sleep(0.3)
        GPIO.output(BuzzerPin, GPIO.HIGH)
        time.sleep(0.3)

# destroy function
def destroy():
    # Turn off buzzer
    GPIO.output(BuzzerPin, GPIO.HIGH)
    # Release resource
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        main()
    # When 'Ctrl+C' is pressed, the child program
    # destroy() will be  executed.
    except KeyboardInterrupt:
        destroy()
