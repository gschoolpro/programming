# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from time import sleep
import wiringpi as pi

delay = 0.2
led_pin = 23
sensor_pin = 18
count = 0

#センサ反応時光らせるのは子どもたちに任せるかも

def sensor_init():  #初期設定
    GPIO.setmode(GPIO.BCM)
    pi.wiringPiSetupGpio() # GPIO名で番号を指定する
    pi.pinMode( led_pin, pi.OUTPUT )
    pi.pinMode( sensor_pin, pi.INPUT)

def main():	#動作設定
    sensor_init()
    while True:
        if( pi.digitalRead( sensor_pin ) == pi.HIGH ):	#センサが感知したとき
            while count < 5:	#ledの点滅
                pi.digitalWrite(led_pin, pi.HIGH)
                sleep(delay * 2)
                pi.digitalWrite(led_pin, pi.LOW)
                sleep(delay)
                count += 1
            count = 0
        else:
            pi.digitalWrite(led_pin, pi.LOW)
        sleep(delay)

if __name__ == '__main__':

    try: #通常時
        main()
    except KeyboardInterrupt: #キーボードが押されたとき
        pass
    finally: #終了時(ctrl+cなど)
        pass

