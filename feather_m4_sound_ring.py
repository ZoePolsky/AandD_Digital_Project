import array
import math
import board
import audiobusio
import time
import neopixel
from digitalio import DigitalInOut, Direction, Pull

pixel_pin = board.D5
num_pixels = 8  # number of leds pixels on the ring

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.6, auto_write=False)

# Remove DC bias before computing RMS.
def mean(values):
    return sum(values) / len(values)


def normalized_rms(values):
    minbuf = int(mean(values))
    samples_sum = sum(float(sample - minbuf) * (sample - minbuf) for sample in values)

    return math.sqrt(samples_sum / len(values))


mic = audiobusio.PDMIn(board.TX, board.D12, sample_rate=16000, bit_depth=16)
samples = array.array("H", [0] * 320)

# Clear the pixels
pixels.fill((0, 0, 0))

while True:
    mic.record(samples, len(samples))
    magnitude = normalized_rms(samples)
    print(int((magnitude) / 200))
    mag = int((magnitude) / 200)
    if mag > 16:
        mag = 16

    for x in range(0, mag):
        pixels[x] = (0, 0, 225)
    pixels.show()
    time.sleep(0.01)
    pixels.fill((0, 0, 0))
