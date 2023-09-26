#print time and date on ESP32-S3 LCD screen

import time
import board
import busio
import adafruit_pcf8523
import terminalio
from adafruit_display_text import bitmap_label

yellowy = 0x99FF22

myI2C = busio.I2C(board.SCL, board.SDA)
rtc = adafruit_pcf8523.PCF8523(myI2C)

days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

if False:   # change to True if you want to write the time!
    #                     year, mon, date, hour, min, sec, wday, yday, isdst
    t = time.struct_time((2023,  9,   26,   11,  49,  00,    3,   -1,    -1))
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

    time.sleep(1) # wait a second

    text = " %s" % (days[t.tm_wday]) + "\n %d/%d/%d" % (t.tm_mon, t.tm_mday, t.tm_year) +"\n %d:%02d:%02d" % (t.tm_hour, t.tm_min, t.tm_sec)
    # Update this to change the size of the text displayed. Must be a whole number.
    scale = 3

    text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=scale, color=yellowy)
    text_area.x = 5
    text_area.y = 20
    board.DISPLAY.show(text_area)

    time.sleep (0.1)

