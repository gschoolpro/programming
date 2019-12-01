import picamera
import time

def main():
    with picamera.PiCamera() as camera:
        camera.resolution = (1024,768)
        camera.start_preview()
        time.sleep(2)
        camera.capture('capture.jpg')

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    pass
