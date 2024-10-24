#works with circuitPython 9

import ipaddress
import ssl
import wifi
import socketpool
import adafruit_requests
import time
import json
import board
import terminalio
from adafruit_display_text import bitmap_label

red = 0xFF0000
purple = 0xFF00FF

# URLs to fetch from
JSON_DATA_URL = 'https://webservices.umoiq.com/api/pub/v1/agencies/sfmta-cis/stopcodes/13548/predictions?key=0be8ebd0284ce712a63f29dcaf7798c4'

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

while True:
    response = requests.get(JSON_DATA_URL)
    #print(response.json())
    muni_route = response.json()[0]['route']['title']
    muni_stop = response.json()[0]['stop']['name']
    muni_eta = response.json()[0]['values'][0]['minutes']
    print(muni_route + " arrives in " + str(muni_eta) + " minutes at " + str(muni_stop) + " stop")
    
    text = f"{muni_route} bus\narrives in \n{muni_eta} minutes at \n{muni_stop} stop."  #\n creates a new line
    scale = 2

    text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=scale, color=purple)
    text_area.x = 10
    text_area.y = 20
    board.DISPLAY.root_group = (text_area)

    time.sleep(30)
