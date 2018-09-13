#sudo apt-get install python3-rpi.gpio

import RPi.GPIO as GPIO
import time
import requests

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

button_1 = 4
button_2 = 17

GPIO.setup(button_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

button_1_toggle = False
button_2_toggle = False


while True:

	try:

		#buttons are low-active
		if not GPIO.input(button_1):
			if not button_1_toggle:
				button_1_toggle = True
				print('Button 1 pressed')
				url = ''
				requests.get(url)
		else:
			button_1_toggle = False


		if not GPIO.input(button_2):
			if not button_2_toggle:
				button_2_toggle = True
				print('Button 2 pressed')
		else:
			button_2_toggle = False


		time.sleep(0.05)
		
	except Exception as e:
		print(str(e))

