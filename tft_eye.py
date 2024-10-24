import board
import time
from displayio import OnDiskBitmap, TileGrid, Group
import terminalio
from adafruit_display_text import bitmap_label

lt_blue = 0x00FFFF
blue = 0x0000FF

main_group = Group()
blinka_img = OnDiskBitmap("images/eye.bmp")  # you must save your image into an images folder on your circuitpy device
print("running")

while True:

    tile_grid = TileGrid(bitmap=blinka_img, pixel_shader=blinka_img.pixel_shader,)  #reference your image here
    main_group.append(tile_grid)
    board.DISPLAY.root_group = (main_group)
    tile_grid.x = board.DISPLAY.width // 2 - blinka_img.width // 2
    
    time.sleep(2)
    main_group.pop(-1) #remove image from the display
    
    my_text = "EYE"    #add your text here
    text_area = bitmap_label.Label(terminalio.FONT, text=my_text, scale=5, color=blue, x=70, y=30)
    main_group.append(text_area)   #add your text to group

    time.sleep(2)
    
    my_text = "SEE U"    #add your text here
    text_area = bitmap_label.Label(terminalio.FONT, text=my_text, scale=5, color=lt_blue, x=35, y=90)
    main_group.append(text_area)   #add your text to group
    
    time.sleep(2)
    main_group.pop(-1) #remove text from the display
