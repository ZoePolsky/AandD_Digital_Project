import array
import math
import board
import audiobusio
import time
from adafruit_featherwing import neopixel_featherwing

neopixel = neopixel_featherwing.NeoPixelFeatherWing()

# Remove DC bias before computing RMS.
def mean(values):
    return sum(values) / len(values)
    
def normalized_rms(values):
    minbuf = int(mean(values))
    samples_sum = sum(
        float(sample - minbuf) * (sample - minbuf)
        for sample in values
    )

    return math.sqrt(samples_sum / len(values))

    
mic = audiobusio.PDMIn(board.TX, board.D12, sample_rate=16000, bit_depth=16)
samples = array.array('H', [0] * 160)

# Clear the screen
neopixel.fill()
neopixel.auto_write = False

while True:
    
    mic.record(samples, len(samples))
    magnitude = normalized_rms(samples)
    print(int((magnitude)/400))
    color=int((magnitude)/400)
    if color > 8:
        color=8
    
    for x in range(0, color):
        for y in range(neopixel.rows - 1, -1, -1):
            neopixel[x, y] = (y * 63, y * 63, 255)
    neopixel.show()
  
    time.sleep(0.01)
    neopixel.fill()
