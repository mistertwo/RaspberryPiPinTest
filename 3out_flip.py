import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)

try:
	while 1:
		GPIO.output(3, GPIO.HIGH)
		print("Going on!")
		GPIO.output(3, True)
		time.sleep(1)
		print("Going off!")
		GPIO.output(3, False)
		time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()
finally:
	GPIO.cleanup
