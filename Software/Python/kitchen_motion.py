#!/usr/bin/env python

import time
import grovepi

pir_sensor = 8
led = 4
motion=0
grovepi.pinMode(pir_sensor,"INPUT")
grovepi.pinMode(led,"OUTPUT")

while True:
	try:
		motion=grovepi.digitalRead(pir_sensor)
		if motion==0 or motion==1:
			if motion==1:
				grovepi.digitalWrite(led,1)
				time.sleep(10)
				grovepi.digitalWrite(led,0)

		time.sleep(.2)

	except KeyboardInterrupt:
		grovepi.digitalWrite(led,0)

	except IOError:
		print ("Error")