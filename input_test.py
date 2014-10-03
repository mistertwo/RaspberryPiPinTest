import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

pin_in = 3
pin_out = 18

GPIO.setup(pin_in, GPIO.IN)
GPIO.setup(pin_out, GPIO.OUT)



wat = 1

try:
	while wat != 0:
		if (GPIO.input(pin_in) == False):
			print("things have been done!")
			servo = GPIO.PWM(pin_out, 50)
		        servo.start(7.5)
        		runtime = 7.5
        		mod = 0.5
        		#achieving lock at 9?
        		while wat != 0:
                		if runtime > 22.5:
                        		mod = 0.975
                		if runtime < 0.5:
                        		mod = 1.025
                		runtime = runtime * mod
                		#print(runtime)
                		#servo.ChangeFrequency(100)
				if (GPIO.input(pin_in) == False):
					runtime = min(runtime * 2, 99)
	               		
				servo.ChangeDutyCycle(runtime)
				wat += 1
				if wat > 200000:
					wat = 0
        		time.sleep(2)
        		servo.stop()

	
		if (GPIO.input(pin_in) == True):
			GPIO.output(pin_out, False)
		#time.sleep(0.5)

except KeyboardInterrupt:
       	GPIO.cleanup()
finally:
       	GPIO.cleanup()
