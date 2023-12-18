#print time and date on ESP32-S3 LCD screen over an image

import time
import board
import busio
import adafruit_pcf8523
import terminalio
from adafruit_display_text import bitmap_label
from displayio import OnDiskBitmap, TileGrid, Group

black = (0,0,0)
lt_blue = 0x00FFFF
blue = 0x0000FF

myI2C = busio.I2C(board.SCL, board.SDA)
rtc = adafruit_pcf8523.PCF8523(myI2C)

main_group = Group()
blinka_img = OnDiskBitmap("images/bow.bmp")  # you must save your image into an images folder on your circuitpy device

tile_grid = TileGrid(bitmap=blinka_img, pixel_shader=blinka_img.pixel_shader,)  #reference your image here
main_group.append(tile_grid)
board.DISPLAY.show(main_group)
tile_grid.x = board.DISPLAY.width // 2 - blinka_img.width // 2




days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

t = rtc.datetime

#First Run display
text = "  %s" % (days[t.tm_wday]) +"\n   %d:%02d" % (t.tm_hour, t.tm_min)
# Update this to change the size of the text displayed. Must be a whole number.
scale = 4
text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=scale, color=black)
text_area.x = 5
text_area.y = 20
main_group.append(text_area)   #add your text to group
board.DISPLAY.show(main_group)

if False:   # change to True if you want to write the time!
    #                     year, mon, date, hour, min, sec, wday, yday, isdst
    t = time.struct_time((2023,  12,   11,   13,  43,  00,    1,   -1,    -1))
    # you must set year, mon, date, hour, min, sec and weekday
    # yearday is not supported, isdst can be set but we don't do anything with it at this time

    print("Setting time to:", t)     # uncomment for debugging
    rtc.datetime = t
    print()

while True:
    t = rtc.datetime
    #print(t)     # uncomment for debugging

    print("The date is %s %d/%d/%d" % (days[t.tm_wday], t.tm_mon, t.tm_mday, t.tm_year))
    print("The time is %d:%02d:%02d" % (t.tm_hour, t.tm_min, t.tm_sec))

    current_min = t.tm_min
    time.sleep (1)
    t = rtc.datetime

    if t.tm_min != current_min:
        main_group.pop(-1) #remove previous text from the display
        text = "  %s" % (days[t.tm_wday]) +"\n   %d:%02d" % (t.tm_hour, t.tm_min)
        # Update this to change the size of the text displayed. Must be a whole number.
        scale = 4

        text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=scale, color=black)
        text_area.x = 5
        text_area.y = 20
        main_group.append(text_area)   #add your text to group
        board.DISPLAY.show(main_group)


