import ipaddress
import ssl
import wifi
import socketpool
import adafruit_requests
import time
import json
import board
import terminalio
import digitalio
from adafruit_display_text import bitmap_label
import neopixel

pixel_pin = board.D5   #the ring data is connected to this pin
num_pixels = 8      #number of leds pixels on the ring

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

red = 0xFF0000
purple = 0xFF00FF

#------------- Buttons -----------#
lastButtonValues = [True, False, False] # buttons D0-D3 default values are High, Low, Low

button0 = digitalio.DigitalInOut(board.D0)
button0.switch_to_input(pull=digitalio.Pull.UP)

button1 = digitalio.DigitalInOut(board.D1)
button1.switch_to_input(pull=digitalio.Pull.DOWN)

button2 = digitalio.DigitalInOut(board.D2)
button2.switch_to_input(pull=digitalio.Pull.DOWN)

#------------- Weather API ---------------------#
# Weather URLs to fetch from
W_APPID = "0e974dbb38ad3719228ac1854b212827" #get api key here: https://openweathermap.org/api
W_JSON_DATA_URL = f"http://api.openweathermap.org/data/2.5/weather?q=94112,us&APPID={W_APPID}&units=imperial"

#------------- MUNI API ---------#
# Muni URLs to fetch from
M_JSON_DATA_URL = 'https://webservices.umoiq.com/api/pub/v1/agencies/sfmta-cis/stopcodes/13548/predictions?key=0be8ebd0284ce712a63f29dcaf7798c4'

#------------- WIFI-------------#

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

#------------- Fetching & Modes -------------#
lastFetch = 0
mode = 0 # Modes are 0 (weather), 1 (muni), and 2(lights)

def weatherMode():
    print("weather mode fetch")
    response = requests.get(W_JSON_DATA_URL)
    weather_data = response.json()
    temperature = weather_data["main"]["temp"]
    location = weather_data["name"]

    text = f"It's currently \n{temperature} degrees \nin {location}."  #\n creates a new line
    scale = 2

    text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=scale, color=red)
    text_area.x = 10
    text_area.y = 20
    board.DISPLAY.root_group = text_area

def muniMode():
    response = requests.get(M_JSON_DATA_URL)
    #print(response.json())
    muni_route = response.json()[0]['route']['title']
    muni_stop = response.json()[0]['stop']['name']
    muni_eta = response.json()[0]['values'][0]['minutes']
    print(muni_route + " arrives in " + str(muni_eta) + " minutes at " + str(muni_stop) + " stop")

    text = f"{muni_route}\narrives in \n{muni_eta} minutes at \n{muni_stop} stop."  #\n creates a new line
    scale = 2

    text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=scale, color=purple)
    text_area.x = 10
    text_area.y = 20
    board.DISPLAY.root_group = text_area

def lightsMode():
    text = "Lights Mode"
    scale = 2

    text_area = bitmap_label.Label(terminalio.FONT, text=text, scale=scale, color=purple)
    text_area.x = 10
    text_area.y = 20
    board.DISPLAY.root_group = text_area

    pixels.fill(red)
    pixels.show()

def clearLights():
    pixels.fill((0,0,0))
    pixels.show()

modeFetch = weatherMode


#------------- Utils -------------#

def checkButtons():
    global lastButtonValues, mode
    global modeFetch
    global lastFetch

    buttonJustPressed = False
    currentButtonValues = [button0.value, button1.value, button2.value]
    ## Below triggers if a button change is detected, and a button is on the "pressed" state
    if ((lastButtonValues != currentButtonValues) and (not currentButtonValues[0] or currentButtonValues[1] or currentButtonValues[2])):
        if (not currentButtonValues[0]):
            mode = 0
            modeFetch = weatherMode
        elif (currentButtonValues[1]):
            mode = 1
            modeFetch = muniMode
        elif (currentButtonValues[2]):
            mode = 2
            modeFetch = lightsMode

        print(f"changing mode to {mode}")
        clearLights()
        lastFetch = 0
        buttonJustPressed = True

    lastButtonValues = currentButtonValues
    return buttonJustPressed

while True:
    currentTime = time.time()
    if (currentTime - lastFetch > 10):
        modeFetch()
        lastFetch = currentTime

    if checkButtons():
        lastFetch = 0

