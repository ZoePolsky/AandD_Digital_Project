import board
import time
import displayio
import terminalio

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

# Setup the file as the bitmap data source
bitmap = displayio.OnDiskBitmap("face.bmp")

# Create a TileGrid to hold the bitmap
tile_grid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)

# Create a Group to hold the TileGrid
group = displayio.Group()

# Add the TileGrid to the Group
group.append(tile_grid)
    
# Add the Group to the Display
display.show(group)
    
# Loop forever so you can enjoy your image
while True:
    
    my_text = "Enjoy"    #add your text here
    total_text = label.Label(terminalio.FONT, text=my_text, scale=2, color=0xFFFFFF, x=70, y=30)
    group.append(total_text)   #add your text to group

    # Add the Group to the Display
    display.show(group)
    
    time.sleep(2)
    group.pop(-1)
    
    my_text = "Life"    #add your text here
    total_text = label.Label(terminalio.FONT, text=my_text, scale=2, color=0xFFFFFF, x=70, y=30)
    group.append(total_text)   #add your text to group
    
    time.sleep(2)
    group.pop(-1)
