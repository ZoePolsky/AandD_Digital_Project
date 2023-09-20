"""
Temperature and Humidity to LCD
"""

import time
import board
import adafruit_ahtx0
import terminalio
from adafruit_display_text import bitmap_label

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
sensor = adafruit_ahtx0.AHTx0(i2c)

lt_green = 0x99FF99

while True:    
    # Update this to change the text displayed.
    text = str(round(sensor.temperature,2)) + " C"
    text += "\n" + str(round(sensor.relative_humidity,2)) + " % Hum"
    
    # Update this to change the size of the text displayed. Must be a whole number.
    scale = 3
    
    text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=scale, color=lt_green)
    text_area.x = 10
    text_area.y = 40
    board.DISPLAY.show(text_area)

    time.sleep (3)
