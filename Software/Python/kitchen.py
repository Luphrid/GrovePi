#!/usr/bin/env python

from datetime import datetime,timedelta
import time
import grovepi

senzormotion = 4
litzmotion = 3
motion=0
grovepi.pinMode(senzormotion,"INPUT")
grovepi.pinMode(litzmotion,"OUTPUT")

sensorz = [0, 1, 2]
lightz = [2, 5, 6]
for senz in sensorz:
    grovepi.pinMode(senz,"INPUT")
for litz in lightz:
    grovepi.pinMode(litz,"OUTPUT")

time.sleep(1)

adc_ref = 5
grove_vcc = 5
full_angle = 300
prevv = [0, 0, 0]
period = timedelta(minutes=1)
next_time = datetime.now() + period
minutes = 0
motion_litz_on = False

while True:
    try:
        # ROTARY LIGHTS
        for i, senz in enumerate(sensorz):
            sensor_value = grovepi.analogRead(senz)
            voltage = round((float)(sensor_value) * adc_ref / 1023, 2)
            degrees = round((voltage * full_angle) / grove_vcc, 2)
            brightness = int(degrees / full_angle * 255)
            if brightness != prevv[i]:
                prevv[i] = brightness
                grovepi.analogWrite(lightz[i],brightness)
        # MOTION LIGHT
        ## Light timeout
        if next_time <= datetime.now():
            minutes += 1
            next_time += period
            grovepi.digitalWrite(litzmotion,0)
            motion_litz_on = False
            
        ## Motion detect
        if motion_litz_on==False:
            motion=grovepi.digitalRead(senzormotion)
            if motion==0 or motion==1:
                if motion==1:
                    grovepi.digitalWrite(litzmotion,1)
                    motion_litz_on = True
    except KeyboardInterrupt:
        for litz in lightz:
            grovepi.analogWrite(litz,0)
        grovepi.digitalWrite(litzmotion,0)
        break
    except IOError:
        print ("Error")
