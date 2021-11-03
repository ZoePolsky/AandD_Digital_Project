# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: Unlicense
"""
based on code by Author: Mark Roberts (mdroberts1243) from Adafruit code
Altered by A. Kleindolph
"""

import board
import time
import displayio
import terminalio

# can try import bitmap_label below for alternative
from adafruit_display_text import label
import adafruit_displayio_sh1107

displayio.release_displays()
# oled_reset = board.D9

# Use for I2C
i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

# SH1107 is vertically oriented 64x128
WIDTH = 128
HEIGHT = 64
BORDER = 2

display = adafruit_displayio_sh1107.SH1107(display_bus, width=WIDTH, height=HEIGHT)

# Make the display context
splash = displayio.Group()
display.show(splash)

while True:
    my_text = "hola"    #add your text here
    text_area2 = label.Label(
    terminalio.FONT, text=my_text, scale=2, color=0xFFFFFF, x=13, y=20
    )
    splash.append(text_area2)   #add your text to splash
    
    display.show(splash)   #anything that is in splash will show on the screen
    time.sleep(2)

    splash.pop(-1)    #remove the last item added to splash
    my_text = "adios"   #add some next text
    text_area2 = label.Label(
    terminalio.FONT, text=my_text, scale=2, color=0xFFFFFF, x=13, y=20
    )
    splash.append(text_area2) #add your text to splash
    
    display.show(splash)    #anything that is in splash will show on the screen
    time.sleep(2)
    splash.pop(-1)    #remove the last item added to splash
