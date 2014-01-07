from time inport sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)
number = 0
prev_input = 0

loop = True
print number
while (loop):
	if(GPIO.input(23) == True):
		number += 1
		print number
		prev_input = input
		sleep(0.5)
		continue
	if(GPIO.input(24) == True):
		number -= 1
		print number
		prev_input = input
		sleep(0.5)
		continue
	if(GPIO.input(25) == True):
		loop = False
		prev_input = input
		sleep(0.5)
		continue
print "End with number at " + str(number)