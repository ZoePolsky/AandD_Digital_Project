# SPDX-FileCopyrightText: 2021 Tim C for Adafruit Industries
# SPDX-License-Identifier: MIT
"""
CircuitPython simple text display demo
"""
import board
import terminalio
import time
from adafruit_display_text import bitmap_label

# Update this to change the text displayed.
text = "Hello!"
# Update this to change the size of the text displayed. Must be a whole number.
scale = 4

text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=scale)
text_area.x = 0
text_area.y = 60
board.DISPLAY.show(text_area)

while True:
    for move in range(-300, 300,1):
        text_area.x = move
        text_area.y = 60
        board.DISPLAY.show(text_area)
        time.sleep(0.01)
