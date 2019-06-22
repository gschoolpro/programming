# -*- coding: utf-8 -*-
#試作品
import RPi.GPIO as GPIO
import time
import wiringpi as pi
import dht11        #gitでクローンする

temp_sensor=23

def temp_init(): #初期設定
    GPIO.setmode(GPIO.BCM)
    pi.wiringPiSetupGpio() # GPIO名で番号を指定する
    pi.pinMode( temp_sensor, pi.INPUT )

def main():     #動作設定

    temp_init() #初期設定の呼び出し

    instance = dht11.DHT11( pin = temp_sensor )
    while True:
        result = instance.read()
        if result.is_valid():
            print("Temperature = ",result.temperature,"C"," Humidity = ",result.humidity,"%")
            time.sleep(1)

if __name__ == '__main__':

    try: #通常時
        main()
    except KeyboardInterrupt: #キーボードが押されたとき
        pass
    finally: #終了時(ctrl+cなど)
        pass
