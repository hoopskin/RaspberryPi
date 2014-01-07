from time inport sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)
number = 0
prev_input = 0

continue = True
while (continue):
	print number
	input = GPIO.input(23)
	if((not prev_input) and input):
		number += 1
		prev_input = input
		sleep(0.05)
		continue
	input = GPIO.input(24)
	if((not prev_input) and input):
		number -= 1
		prev_input = input
		sleep(0.05)
		continue
	input = GPIO.input(25)
	if((not prev_input) and input):
		continue = False
		prev_input = input
		sleep(0.05)
		continue