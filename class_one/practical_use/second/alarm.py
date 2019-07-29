import RPi.GPIO as GPIO
import time
import datetime

# Set #18 as buzzer pin
BuzzerPin = 18
# Set #17 as LED pin
LEDPin = 17

# restore time that program starts working
start = time.time()

# set timer
settime = 5

def setup():
    GPIO.setwarnings(False)
    # Set the GPIO modes to BCM Numbering
    GPIO.setmode(GPIO.BCM)
    # Set BuzzerPin's mode to output, 
    # and initial level to High(3.3v)
    GPIO.setup(BuzzerPin, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(LEDPin, GPIO.OUT, initial=GPIO.LOW)

def main():
    t = time.time() - start
    while t < settime:
	print int(settime) - int(t)
	time.sleep(1)
	t = time.time() - start
    while t >= settime:
	print "Good Morning!!"
	for i in range(4):
	    GPIO.output(BuzzerPin, GPIO.LOW)
	    GPIO.output(LEDPin, GPIO.HIGH)
	    time.sleep(0.05)
	    GPIO.output(BuzzerPin, GPIO.HIGH)
	    GPIO.output(LEDPin, GPIO.LOW)
	    time.sleep(0.05)
	time.sleep(0.5)

# If run this script directly, do:
if __name__ == '__main__':
    setup()
    try:
	main()
    except KeyboardInterrupt:
        # Turn off buzzer
        GPIO.output(BuzzerPin, GPIO.HIGH)
	# Turn off LED
	GPIO.output(LEDPin, GPIO.LOW)
        # Release resource
        GPIO.cleanup() 
