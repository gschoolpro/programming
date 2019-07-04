# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from time import sleep
import wiringpi as pi

GPIO.setmode(GPIO.BCM)
delay = 0.2
sensor_pin = 18
count = 0

# ピンの名前を変数として定義
SPICS = 8
SPIMISO = 9
SPIMOSI = 10
SPICLK = 11

# SPI通信用の入出力を定義
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICS, GPIO.OUT)

LED = 25
GPIO.setup(LED, GPIO.OUT)

def sensor_init(adcnum, clockpin, mosipin, misopin, cspin):  #初期設定
    if adcnum > 7 or adcnum < 0:
        return -1

    GPIO.output(cspin, GPIO.HIGH)
    GPIO.output(clockpin, GPIO.LOW)
    GPIO.output(cspin, GPIO.LOW)

    commandout = adcnum
    commandout |= 0x18  # スタートビット＋シングルエンドビット
    commandout <<= 3    # LSBから8ビット目を送信するようにする

    for i in range(5):
        # LSBから数えて8ビット目から4ビット目までを送信
        if commandout & 0x80:
            GPIO.output(mosipin, GPIO.HIGH)
        else:
            GPIO.output(mosipin, GPIO.LOW)
        commandout <<= 1
        GPIO.output(clockpin, GPIO.HIGH)
        GPIO.output(clockpin, GPIO.LOW)
    adcout = 0
    # 13ビット読む（ヌルビット＋12ビットデータ）
    for i in range(13):
        GPIO.output(clockpin, GPIO.HIGH)
        GPIO.output(clockpin, GPIO.LOW)
        adcout <<= 1
        if i>0 and GPIO.input(misopin)==GPIO.HIGH:
            adcout |= 0x1
    GPIO.output(cspin, GPIO.HIGH)
    return adcout



def main():	#動作設定
    while True:
        
        inputVal0 = sensor_init(0, SPICLK, SPIMOSI, SPIMISO, SPICS)

        if inputVal0 < 100:
            print("dark")
        else:
            print("blight")

        print(inputVal0)
        sleep(1)

if __name__ == '__main__':

    try: #通常時
        main()
    except KeyboardInterrupt: #キーボードが押されたとき
        pass
    finally: #終了時(ctrl+cなど)
        GPIO.cleanup()

