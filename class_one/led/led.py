# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import wiringpi as pi

led_pin = 23

def led_init(): #初期設定
    GPIO.setmode(GPIO.BCM)
    pi.wiringPiSetupGpio() # GPIO名で番号を指定する
    pi.pinMode( led_pin, pi.OUTPUT )

def main():

    led_init() #初期設定の呼び出し
 
    while True: #繰り返しの処理
        pi.digitalWrite(led_pin, pi.HIGH)
        time.sleep(3)
        #ここまで繰り返す

if __name__ == '__main__':

    try: #通常時
        main()
    except KeyboardInterrupt: #キーボードが押されたとき
        pass
    finally: #終了時(ctrl+cなど)
        pi.digitalWrite(led_pin, pi.LOW)
        
