import RPi.GPIO as GPIO
import time
import select
import sys
import curses

#check into signal.signal to handle pin disabling on close!


GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)

try:
	servo = GPIO.PWM(3, 50)
	servo.start(7.5)
	time.sleep(2)
	runtime = 7.5
	mod = 0.5
	#achieving lock at 9?
	while 1:
		if runtime > 12.5:
			mod = 0.95
		if runtime < 2.5:
			mod = 1.05
		runtime = runtime * mod
		print(runtime)
		servo.ChangeDutyCycle(runtime)
		#servo.ChangeFrequency(100)
	time.sleep(2)
	servo.stop()
except KeyboardInterrupt:
	servo.stop()
	GPIO.cleanup()
finally:
	servo.stop()
	GPIO.cleanup()
