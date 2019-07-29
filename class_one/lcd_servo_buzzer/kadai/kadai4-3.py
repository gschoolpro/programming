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

def main():
    while True:
	GPIO.output(BuzzerPin, GPIO.LOW)
	time.sleep(0.05)
	GPIO.output(BuzzerPin, GPIO.HIGH)
	time.sleep(0.05)

# If run this script directly, do:
if __name__ == '__main__':
    setup()
    try:
	main()
    except KeyboardInterrupt:
        # Turn off buzzer
        GPIO.output(BuzzerPin, GPIO.HIGH)
        # Release resource
        GPIO.cleanup()    

