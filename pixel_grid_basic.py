import board
import time
from adafruit_featherwing import neopixel_featherwing

neopixel = neopixel_featherwing.NeoPixelFeatherWing()
neopixel.auto_write = False

red = (255,0,0)      #create a color

#clear the screen
neopixel.fill()   #fill all pixels with no color
neopixel.show()   # show it
    
while True:
    
    neopixel[0, 0] = (red)  #fill one pixel with red at location 0,0
    neopixel.show()             # show it
    time.sleep(2)
    
    neopixel.fill()   #fill all pixels with no color
    neopixel.show()   # show it
    time.sleep(1)
    
    neopixel.fill(red)   #fill all pixels with red
    neopixel.show()      # show it
    time.sleep(2)
    
    neopixel.fill()   #fill all pixels with no color
    neopixel.show()   # show it
    time.sleep(1)
