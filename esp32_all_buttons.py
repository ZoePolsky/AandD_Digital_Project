import board
import digitalio
import terminalio
from adafruit_display_text import bitmap_label

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

button0 = digitalio.DigitalInOut(board.D0)
button0.switch_to_input(pull=digitalio.Pull.UP)

button1 = digitalio.DigitalInOut(board.D1)
button1.switch_to_input(pull=digitalio.Pull.DOWN)

button2 = digitalio.DigitalInOut(board.D2)
button2.switch_to_input(pull=digitalio.Pull.DOWN)

red = 0xFF0000
purple = 0xFF00FF
blue = 0x0000FF

while True:
    if not button0.value:
        text = "button 0"
        scale = 3

        text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=scale, color=red)
        text_area.x = 10
        text_area.y = 20
        board.DISPLAY.root_group = text_area
        
    if button1.value:
        text = "button 1"
        scale = 3

        text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=scale, color=purple)
        text_area.x = 10
        text_area.y = 60
        board.DISPLAY.root_group = text_area
    
    if button2.value:
        text = "button 2"
        scale = 3

        text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=scale, color=blue)
        text_area.x = 10
        text_area.y = 120
        board.DISPLAY.root_group = text_area
