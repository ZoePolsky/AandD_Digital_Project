"""
Temperature and Humidity to LCD - circuitPython 9
"""

# SPDX-FileCopyrightText: Copyright (c) 2020 ladyada for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_sht4x
import terminalio
from adafruit_display_text import bitmap_label

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
sht = adafruit_sht4x.SHT4x(i2c)
print("Found SHT4x with serial number", hex(sht.serial_number))

lt_green = 0x99FF99

sht.mode = adafruit_sht4x.Mode.NOHEAT_HIGHPRECISION
# Can also set the mode to enable heater
# sht.mode = adafruit_sht4x.Mode.LOWHEAT_100MS
print("Current mode is: ", adafruit_sht4x.Mode.string[sht.mode])

while True:
    temperature, relative_humidity = sht.measurements
    print("Temperature: %0.1f C" % temperature)
    print("Humidity: %0.1f %%" % relative_humidity)
    print("")
    time.sleep(1)
    
    # Update this to change the text displayed.
    text = str(round(temperature,2)) + " C"
    text += "\n" + str(round(relative_humidity,2)) + " % Hum"
    
    # Update this to change the size of the text displayed. Must be a whole number.
    scale = 3
    
    text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=scale, color=lt_green)
    text_area.x = 10
    text_area.y = 40
    board.DISPLAY.root_group = (text_area)

    time.sleep (3)


