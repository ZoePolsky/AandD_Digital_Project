#works with circuitPython 9

import ipaddress
import ssl
import wifi
import socketpool
import adafruit_requests
import time
import json
import board
import random
import terminalio
from adafruit_display_text import bitmap_label

red = 0xFF0000
purple = 0xFF00FF

# URLs to fetch from
API_KEY = "YOUR KEY HERE" #get a key here https://developer.nytimes.com/
JSON_DATA_URL = f'https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key={API_KEY}' 

# Get wifi details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

wifi.radio.connect(secrets["ssid"], secrets["password"])
print("Connected to %s!"%secrets["ssid"])
print("My IP address is", wifi.radio.ipv4_address)

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())


def wrap_nicely(string, max_chars):
    """A helper that will return the string with word-break wrapping.
    :param str string: The text to be wrapped.
    :param int max_chars: The maximum number of characters on a line before wrapping.
    """
    string = string.replace('\n', '').replace('\r', '') # strip confusing newlines
    words = string.split(' ')
    the_lines = []
    the_line = ""
    for w in words:
        if len(the_line+' '+w) <= max_chars:
            the_line += ' '+w
        else:
            the_lines.append(the_line)
            the_line = w
    if the_line:
        the_lines.append(the_line)
    the_lines[0] = the_lines[0][1:]
    the_newline = ""
    for w in the_lines:
        the_newline += '\n'+w
    return the_newline

while True:
    response = requests.get(JSON_DATA_URL)
    data = response.json()
    random_nyt = random.randint(0,6)
    headline = data["results"][random_nyt]["title"]
    print(headline)

    text = wrap_nicely(headline,20)
    
    scale = 2
    text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=scale, color=purple)
    text_area.x = 0
    text_area.y = 0
    board.DISPLAY.root_group = (text_area)

    time.sleep(60)
