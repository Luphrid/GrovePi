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
p0 = 0
p1 = 1
p2 = 2

# Connect the LED to digital port D5
# SIG,NC,VCC,GND
l0 = 5
l1 = 6
l2 = 7

grovepi.pinMode(p0,"INPUT")
#grovepi.pinMode(p1,"INPUT")
#grovepi.pinMode(p2,"INPUT")
grovepi.pinMode(l0,"OUTPUT")
#grovepi.pinMode(l1,"OUTPUT")
#grovepi.pinMode(l2,"OUTPUT")
time.sleep(1)

# Reference voltage of ADC is 5v
adc_ref = 5

# Vcc of the grove interface is normally 5v
grove_vcc = 5

# Full value of the rotary angle is 300 degrees, as per it's specs (0 to 300)
full_angle = 300

while True:
    try:
        # Read sensor value from potentiometer
        sensor_value0 = grovepi.analogRead(p0)
        #sensor_value1 = grovepi.analogRead(p1)
        #sensor_value2 = grovepi.analogRead(p2)

        # Calculate voltage
        voltage0 = round((float)(sensor_value0) * adc_ref / 1023, 2)
        #voltage1 = round((float)(sensor_value1) * adc_ref / 1023, 2)
        #voltage2 = round((float)(sensor_value2) * adc_ref / 1023, 2)

        # Calculate rotation in degrees (0 to 300)
        degrees0 = round((voltage0 * full_angle) / grove_vcc, 2)
        #degrees1 = round((voltage1 * full_angle) / grove_vcc, 2)
        #degrees2 = round((voltage2 * full_angle) / grove_vcc, 2)

        # Give PWM output to LED
        grovepi.digitalWrite(l0,1 if degrees0 > 0 else 0)
        #grovepi.digitalWrite(l1,1 if degrees1 > 0 else 0)
        #grovepi.digitalWrite(l2,1 if degrees2 > 0 else 0)
        
        print("Sensor1 sensor_value = %d voltage = %.2f degrees = %.1f" %(sensor_value0, voltage0, degrees0))
        print("Sensor1 sensor_value = %d voltage = %.2f degrees = %.1f" %(sensor_value1, voltage1, degrees1))
        print("Sensor1 sensor_value = %d voltage = %.2f degrees = %.1f" %(sensor_value2, voltage2, degrees2))
    except KeyboardInterrupt:
        grovepi.digitalWrite(l0,0)
        #grovepi.digitalWrite(l1,0)
        #grovepi.digitalWrite(l2,0)
        break
    except IOError:
        print ("Error")
