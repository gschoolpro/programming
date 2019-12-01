# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from time import sleep
import wiringpi as pi

delay = 0.2
buzzer_pin = 25
led_pin = 23
sensor_pin = 18
count = 0

E = 265

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)

pi.wiringPiSetupGpio() # GPIO名で番号を指定する

pi.softToneCreate(buzzer_pin)
pi.pinMode( led_pin, pi.OUTPUT )
pi.pinMode( sensor_pin, pi.INPUT)

while True:
    if( pi.digitalRead( sensor_pin ) == pi.HIGH ):
        while count < 5:
            pi.softToneWrite(buzzer_pin, E)
            pi.digitalWrite(led_pin, pi.HIGH)
            sleep(delay * 2)
            pi.softToneWrite(buzzer_pin, 0)
            pi.digitalWrite(led_pin, pi.LOW)
            sleep(delay)
            count += 1
        count = 0
    else:
        pi.softToneWrite(buzzer_pin, 0)
        pi.digitalWrite(led_pin, pi.LOW)
    sleep(delay)
#GPIO.cleanup()
