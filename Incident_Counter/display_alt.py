import board
import neopixel

leds = neopixel.NeoPixel(board.D18, 21, auto_write=False)
light1 = [1, ]
lines = []

def setDisplay(number):
    split = [int(x) for x in str(number)]
    off()
    for place in range(3):
        if split[place] == 0:
            on(1)
            on(2)
            on(3)
            on(4)
            on(5)
            on(6)
        if split[place] == 1:
            on(1)
            on(6)
        if split[place] == 2:
            on(5)
            on(6)
            on(7)
            on(3)
            on(2)
        if split[place] == 3:
            on(5)
            on(6)
            on(7)
            on(1)
            on(2)
        if split[place] == 4:
            on(4)
            on(7)
            on(6)
            on(1)
        if split[place] == 5:
            on(5)
            on(4)
            on(7)
            on(1)
            on(2)
        if split[place] == 6:
            on(5)
            on(4)
            on(3)
            on(2)
            on(1)
            on(7)
        if split[place] == 7:
            on(5)
            on(6)
            on(1)
        if split[place] == 8:
            on(1)
            on(2)
            on(3)
            on(4)
            on(5)
            on(6)
            on(7)
        if split[place] == 9:
            on(7)
            on(4)
            on(5)
            on(6)
            on(1)
            on(2)

setDisplay(0)

def off():
    for i in range(3):
        for j in range(21):
            leds[j] = (0,0,0)

def on(lightNum):
    for i in range(3):
        leds[3(lightnum) + i] = (255, 0, 0)
