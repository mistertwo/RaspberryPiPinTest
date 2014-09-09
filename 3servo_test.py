import RPi.GPIO as GPIO
import time
import select
import sys
import curses

#check into signal.signal to handle pin disabling on close!


GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)

try:
	while 1:
		GPIO.output(3, GPIO.HIGH)
		print("Going on!")
		GPIO.output(3, True)
		time.sleep(.0001)
		print("Going off!")
		GPIO.output(3, False)
		time.sleep(.00001)
except KeyboardInterrupt:
	GPIO.cleanup()
finally:
	GPIO.cleanup
