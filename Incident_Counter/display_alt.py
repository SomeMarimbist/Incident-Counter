import board
import neopixel

leds = neopixel.NeoPixel(board.D18, 21, bpp=3)
light1 = [1, ]
lines = []


def off():
    for i in range(3):
        for j in range(21):
            leds[j] = (0,0,0)

def on(lightNum):
    for i in range(3):
        leds[(lightNum*3) + i] = (255, 0, 0)
        print(lightNum)


def setDisplay(number):
    split = [0, 0, 0]
    temp = [int(x) for x in str(number)]
    for i in len(temp):
        split[(3 - len(temp)+ i)] = temp(i)
    off()
    for place in range(3):
        if split[place] == 0:
            on(0)
            on(1)
            on(2)
            on(3)
            on(4)
            on(5)
        if split[place] == 1:
            on(0)
            on(5)
        if split[place] == 2:
            on(4)
            on(5)
            on(6)
            on(2)
            on(1)
        if split[place] == 3:
            on(4)
            on(5)
            on(6)
            on(0)
            on(1)
        if split[place] == 4:
            on(3)
            on(6)
            on(5)
            on(0)
        if split[place] == 5:
            on(4)
            on(3)
            on(6)
            on(0)
            on(1)
        if split[place] == 6:
            on(4)
            on(3)
            on(2)
            on(1)
            on(0)
            on(6)
        if split[place] == 7:
            on(4)
            on(5)
            on(0)
        if split[place] == 8:
            on(0)
            on(1)
            on(2)
            on(3)
            on(4)
            on(5)
            on(6)
        if split[place] == 9:
            on(6)
            on(3)
            on(4)
            on(5)
            on(0)
            on(1)
        leds.show()

setDisplay(1)
