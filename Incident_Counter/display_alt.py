import board
import neopixel
import time

leds = neopixel.NeoPixel(board.D18, 63, bpp=3)


def off():
    for j in range(63):
            leds[j] = (0,0,0)

def on(lightNum, digit):
    for i in range(3):
        leds[(digit*21) + (lightNum*3) + i] = (255, 0, 0)
        print((digit*21) + (lightNum*3) + i)


def setDisplay(number):
    split = [0, 0, 0]
    temp = [int(x) for x in str(number)]
    length = len(temp)
    for i in range(length):
        split[(3 - length + i)] = temp[i]
    off()
    if split == [0, 6, 9]:
        rainbow()
    for place in range(3):
        if split[place] == 0:
            on(0, place)
            on(1, place)
            on(2, place)
            on(3, place)
            on(4, place)
            on(5, place)
        if split[place] == 1:
            on(0, place)
            on(5, place)
        if split[place] == 2:
            on(4, place)
            on(5, place)
            on(6, place)
            on(2, place)
            on(1, place)
        if split[place] == 3:
            on(4, place)
            on(5, place)
            on(6, place)
            on(0, place)
            on(1, place)
        if split[place] == 4:
            on(3, place)
            on(6, place)
            on(5, place)
            on(0, place)
        if split[place] == 5:
            on(4, place)
            on(3, place)
            on(6, place)
            on(0, place)
            on(1, place)
        if split[place] == 6:
            on(4, place)
            on(3, place)
            on(2, place)
            on(1, place)
            on(0, place)
            on(6, place)
        if split[place] == 7:
            on(4, place)
            on(5, place)
            on(0, place)
        if split[place] == 8:
            on(0, place)
            on(1, place)
            on(2, place)
            on(3, place)
            on(4, place)
            on(5, place)
            on(6, place)
        if split[place] == 9:
            on(6, place)
            on(3, place)
            on(4, place)
            on(5, place)
            on(0, place)
            on(1, place)
    leds.show()

def rainbow():
    while True:
        for j in range(255):
            for i in range(63):
                pixel_index = (i * 256 // 63) + j
                leds[i] = wheel(pixel_index & 255)
            for j in range(18, 21):
                leds[j] = (0,0,0)
            for j in range(36, 39):
                leds[j] = (0,0,0)
            for j in range(48, 51):
                leds[j] = (0,0,0)
            
            leds.show()
            time.sleep(0.5)
#Wheel is used by the rainbow to...rainbow
def wheel(pos):
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b)