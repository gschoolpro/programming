# -*- coding: utf-8 -*-
#試作品
import RPi.GPIO as GPIO
import time
import wiringpi as pi
import dht11        #gitでクローンする

temp_sensor=23 #GPIO23に接続

def temp_init(): #初期設定
    GPIO.setmode(GPIO.BCM)
    pi.wiringPiSetupGpio() # GPIO名で番号を指定する
    pi.pinMode( temp_sensor, pi.INPUT ) #温湿度センサのデータを入力として扱う

def main():     #動作設定

    temp_init() #初期設定の呼び出し

    instance = dht11.DHT11( pin = temp_sensor )  #温湿度センサのデータをinstanceに格納
    while True:
        result = instance.read() #resultにデータを読ませる
        if result.is_valid(): #もしresultにデータが入っている場合
            print("Temperature = ",result.temperature,"C"," Humidity = ",result.humidity,"%") #データにある温度と湿度を画面に表示
            time.sleep(1)

if __name__ == '__main__':

    try: #通常時
        main()
    except KeyboardInterrupt: #キーボードが押されたとき
        pass
    finally: #終了時(ctrl+cなど)
        GPIO.cleanup() #GPIOの終了
