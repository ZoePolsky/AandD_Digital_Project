# Circuit Playground NeoPixel
import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2, auto_write=False)

BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)

while True:
    pixels.fill(BLUE)   #turn on all pixels
    pixels.show()
    time.sleep(0.5)
    pixels[1]=RED      #turn on 2nd pixel on left side
    pixels.show()
    time.sleep(1.0)
