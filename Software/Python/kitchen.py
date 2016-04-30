#!/usr/bin/env python
#
# GrovePi Example for using the Grove Rotary Angle Sensor (Potentiometer) and the Grove LED to create LED sweep
#
# Modules:
#	 http://www.seeedstudio.com/wiki/Grove_-_Rotary_Angle_Sensor
#	 http://www.seeedstudio.com/wiki/Grove_-_LED_Socket_Kit
# The GrovePi connects the Raspberry Pi and Grove sensors.  You can learn more about GrovePi here:  http://www.dexterindustries.com/GrovePi
#
# Have a question about this example?  Ask on the forums here:  http://www.dexterindustries.com/forum/?forum=grovepi
#
'''
## License

The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2015  Dexter Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''


import time
import grovepi

# Connect the Grove Rotary Angle Sensor to analog port A0
# SIG,NC,VCC,GND
ps = array(0, 1, 2)
# Connect the LED to digital port D5
# SIG,NC,VCC,GND
ls = array(5, 6, 7)

for p in ps:
    grovepi.pinMode(p,"INPUT")
    
for l in ls:
    grovepi.pinMode(l,"OUTPUT")

time.sleep(1)

adc_ref = 5
grove_vcc = 5
full_angle = 300
prev = array(0, 0, 0)

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
