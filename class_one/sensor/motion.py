# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from time import sleep
import wiringpi as pi

delay = 0.2
sensor_pin = 18
count = 0


def sensor_init():  #初期設定
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buzzer_pin, GPIO.OUT)
    pi.wiringPiSetupGpio() # GPIO名で番号を指定する
    pi.pinMode( led_pin, pi.OUTPUT )
    pi.pinMode( sensor_pin, pi.INPUT)

def main():	#動作設定
    while True:
        if( pi.digitalRead( sensor_pin ) == pi.HIGH ):	#センサが感知したとき
            print("There are people.")
            sleep(delay)
    
        elif( pi.digitalRead( sensor_pin ) == pi.HIGH ):
            print("There aren't no people.")
            sleep(delay)

if __name__ == '__main__':

    try: #通常時
        main()
    except KeyboardInterrupt: #キーボードが押されたとき
        pass
    finally: #終了時(ctrl+cなど)
        pass

