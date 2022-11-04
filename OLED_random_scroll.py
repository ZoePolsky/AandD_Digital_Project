import board
import time
import displayio
import terminalio
import random

# can try import bitmap_label below for alternative
from adafruit_display_text import label
import adafruit_displayio_sh1107

displayio.release_displays()
# oled_reset = board.D9

WIDTH = 128
HEIGHT = 64
BORDER = 2

# Use for I2C
i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

display = adafruit_displayio_sh1107.SH1107(display_bus, width=WIDTH, height=HEIGHT)


    
# Loop forever so you can enjoy your image
while True:
    x_loc = random.randint(0,WIDTH-50)
    for y_loc in range (-50,70,5):
        # Setup the file as the bitmap data source
        bitmap = displayio.OnDiskBitmap("face.bmp")
        # Create a TileGrid to hold the bitmap
        tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader,x=x_loc, y=y_loc)
        # Create a Group to hold the TileGrid
        group = displayio.Group()
        # Add the TileGrid to the Group
        group.append(tile_grid)
        # Add the Group to the Display
        display.show(group)
        time.sleep(0.1)
        group.pop(-1)
    
    x_loc = random.randint(0,WIDTH-100)
    y_loc = random.randint(0,HEIGHT-10)
    my_text = "deal with it"    #add your text here
    total_text = label.Label(terminalio.FONT, text=my_text, scale=1, color=0xFFFFFF, x=x_loc, y=y_loc)
    group.append(total_text)   #add your text to group
    
    display.show(group)   #anything that is in group will show on the screen
    time.sleep(2)

    group.pop(-1)    #remove the last item added to group
