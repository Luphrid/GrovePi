#!/usr/bin/env python

import time
import grovepi

ps = [0, 1, 2]
ls = [5, 6, 7]

for p in ps:
    grovepi.pinMode(p,"INPUT")
    
for l in ls:
    grovepi.pinMode(l,"OUTPUT")

time.sleep(1)

adc_ref = 5
grove_vcc = 5
full_angle = 300
prev = [0, 0, 0]

while True:
    try:
        for i, p in enumerate(ps):
            sensor_value = grovepi.analogRead(p)
            voltage = round((float)(sensor_value) * adc_ref / 1023, 2)
            degrees = round((voltage * full_angle) / grove_vcc, 2)
            brightness = int(degrees / full_angle * 255)
            if brightness != prev[i]:
                prev[i] = brightness
                grovepi.analogWrite(ls[i],brightness)
            
    except KeyboardInterrupt:
        for l in ls:
            grovepi.analogWrite(l,0)
        break
    except IOError:
        print ("Error")
