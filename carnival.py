import RPi.GPIO as GPIO
import time
import select
import sys
import curses

#check into signal.signal to handle pin disabling on close!

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)

GPIO.output(3,GPIO.HIGH)

def turnOn(pin):
	GPIO.output(pin, True)

def turnOff(pin):
	GPIO.output(pin, False)

def blink(pin,duration=1,interval=50):
	sleepFor = 1.0 / interval
	for i in range(0,duration):
		turnOn(pin)
		time.sleep(sleepFor)
		turnOff(pin)
		time.sleep(sleepFor)

try:
	print('Running....')
	turnOff(8)
	turnOff(3)
	turnOff(5)
	turnOff(7)
	while 1:
		blink(8)
		blink(3)
		blink(5)
		blink(7)

except KeyboardInterrupt:
	print('Shutting down...')
	GPIO.cleanup()

finally:
	print('Done!')
	GPIO.cleanup



