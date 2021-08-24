# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
# Adapted by A. Kleindolph July 2021

import board
import adafruit_ahtx0
import time
from math import sqrt, cos, sin, radians
from adafruit_featherwing import neopixel_featherwing

neopixel = neopixel_featherwing.NeoPixelFeatherWing()

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA
sensor = adafruit_ahtx0.AHTx0(i2c)

# Clear the screen
neopixel.fill()

# Start the Animation
neopixel.auto_write = False
while True:
    
    print("\nTemperature: %0.1f C" % sensor.temperature)
    print("Humidity: %0.1f %%" % sensor.relative_humidity)
    
    if sensor.temperature >= 25:
        neopixel.fill((255, 0, 0))
        neopixel.show()
    else:
        neopixel.fill((0, 255, 0))
        neopixel.show()
        
    time.sleep(1)
    
