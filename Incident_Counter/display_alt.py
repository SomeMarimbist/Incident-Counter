import board
import neopixel

leds = neopixel.NeoPixel(board.D18, 63, bpp=3)


def off():
    for j in range(63):
            leds[j] = (0,0,0)

def on(lightNum, digit):
    for i in range(3):
        leds[digit*21 + (lightNum*3) + i] = (255, 0, 0)


def setDisplay(number):
    split = [0, 0, 0]
    temp = [int(x) for x in str(number)]
    print(temp)
    length = len(temp)
    for i in range(length):
        split[(3 - length + i)] = temp[i]
    off()
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

