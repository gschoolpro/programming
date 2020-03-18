# -*- coding: utf-8 -*-
import picamera
import time

def main():
    with picamera.PiCamera() as camera:
        camera.resolution = (1024,768)  # 画像の大きさの指定
        camera.start_preview()
        time.sleep(2)
        camera.capture('capture.jpg')  # 'capture.jpg'で保存

if __name__ == '__main__':
  try:  # 通常時
    main()
  except KeyboardInterrupt:  # キーボードが押されたとき
    pass
  finally:  # 終了時(ctrl+cなど)
    pass
