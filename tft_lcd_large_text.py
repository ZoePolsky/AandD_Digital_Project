# SPDX-FileCopyrightText: 2021 Tim C for Adafruit Industries
# SPDX-License-Identifier: MIT
"""
CircuitPython simple text display demo
"""
import board
import time
import terminalio
from adafruit_display_text import bitmap_label

red = 0xFF0000
purple = 0xFF00FF

while True:
    # Update this to change the text displayed.
    text = "Hello, toads!"
    # Update this to change the size of the text displayed. Must be a whole number.
    scale = 3

    text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=scale, color=red)
    text_area.x = 10
    text_area.y = 50
    board.DISPLAY.show(text_area)

    time.sleep (0.5)
    
    text = "Hello, frogs!"
    text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=scale, color=purple)
    text_area.x = 10
    text_area.y = 50
    board.DISPLAY.show(text_area)
    time.sleep (0.5)
